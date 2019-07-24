package monitor.dashboard.demo.controller;

import org.json.JSONArray;
import org.json.JSONObject;
import org.springframework.boot.jackson.JsonObjectSerializer;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@RestController
public class MainController {

    @RequestMapping(path = "/", method = {RequestMethod.GET, RequestMethod.POST})
    public String index() {
        JSONObject response = new JSONObject();
        response.put("status", "application is running");
        return response.toString();
    }

    @RequestMapping(path = "/search", method = {RequestMethod.GET, RequestMethod.POST})
    public String search() {
        return "[\"detail_board\",\"summary_board\"]";
    }


    @RequestMapping(path = "/query", method = {RequestMethod.GET, RequestMethod.POST})
    public String query(@RequestBody Map<String, Object> payload) {
        System.out.println(payload);
        return null;
    }
}
