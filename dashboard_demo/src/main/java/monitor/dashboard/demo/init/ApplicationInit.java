package monitor.dashboard.demo.init;

import monitor.dashboard.demo.utils.ElasticHelper;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class ApplicationInit implements CommandLineRunner {

    @Autowired
    private ElasticHelper elasticHelper;

    @Override
    public void run(String... args) throws Exception {
        System.out.printf("Init elastic data here");

        JSONObject jsonObject = new JSONObject();
        jsonObject.put("cr_number", "cr1234");
        elasticHelper.insertData("test", "1", jsonObject.toString());
    }
}