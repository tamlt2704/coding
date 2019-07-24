package monitor.dashboard.demo.utils;

import org.apache.http.HttpHost;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.action.search.*;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.common.unit.TimeValue;
import org.elasticsearch.common.xcontent.XContentType;
import org.elasticsearch.index.query.QueryBuilder;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.search.Scroll;
import org.elasticsearch.search.SearchHit;
import org.elasticsearch.search.SearchHits;
import org.elasticsearch.search.builder.SearchSourceBuilder;
import org.json.JSONObject;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static org.elasticsearch.index.query.QueryBuilders.matchQuery;

@Component
public class ElasticHelper {
    private RestHighLevelClient client;
    final Scroll scroll = new Scroll(TimeValue.timeValueMinutes(1L));

    public ElasticHelper(/*String host, String port*/) {
        String host = "localhost";
        String port = "9200";
        client = new RestHighLevelClient(
                RestClient.builder(new HttpHost(host, Integer.parseInt(port), "http")));
    }

    public boolean insertData(String indexName, String id, String jsonString) {
        try {
            IndexRequest request = new IndexRequest(indexName);
            request.id(id);
            request.source(jsonString, XContentType.JSON);
            client.index(request, RequestOptions.DEFAULT);
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
        return true;
    }

    public List<JSONObject> getCrJrData() {
        List<JSONObject> crjrlist = new ArrayList<>();

        SearchRequest searchRequest = new SearchRequest("crjr");
        SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
        searchSourceBuilder.query(QueryBuilders.matchAllQuery());
        searchSourceBuilder.size(10);
        searchRequest.source(searchSourceBuilder);
        searchRequest.scroll(TimeValue.timeValueMinutes(1L));

        SearchResponse searchResponse = null;
        try {
            searchResponse = client.search(searchRequest, RequestOptions.DEFAULT);
        } catch (IOException e) {
            e.printStackTrace();
        }
        String scrollId = searchResponse.getScrollId();
        SearchHit[] searchHits = searchResponse.getHits().getHits();
        System.out.println("total = " + searchResponse.getHits().getTotalHits());

        crjrlist = Stream.of(searchHits).map(x -> x.getSourceAsMap()).map(x->new JSONObject(x)).collect(Collectors.toList());
        while (searchHits != null && searchHits.length > 0) {
            SearchScrollRequest scrollRequest = new SearchScrollRequest(scrollId);
            scrollRequest.scroll(scroll);
            try {
                searchResponse = client.scroll(scrollRequest, RequestOptions.DEFAULT);
            } catch (IOException e) {
                e.printStackTrace();
            }
            scrollId = searchResponse.getScrollId();
            searchHits = searchResponse.getHits().getHits();

            crjrlist.addAll(Stream.of(searchHits).map(x -> x.getSourceAsMap()).map(x -> new JSONObject(x)).collect(Collectors.toList()));
        }

        ClearScrollRequest clearScrollRequest = new ClearScrollRequest();
        clearScrollRequest.addScrollId(scrollId);
        ClearScrollResponse clearScrollResponse = null;
        try {
            clearScrollResponse = client.clearScroll(clearScrollRequest, RequestOptions.DEFAULT);
        } catch (IOException e) {
            e.printStackTrace();
        }
        boolean succeeded = clearScrollResponse.isSucceeded();

        System.out.println(crjrlist.size());
        return crjrlist;
    }
}