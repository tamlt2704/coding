package monitor.dashboard.demo.schedule;

import monitor.dashboard.demo.utils.DataSimulator;
import monitor.dashboard.demo.utils.ElasticHelper;
import org.json.JSONObject;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class SchedTask {
    DataSimulator dataSimulator = new DataSimulator();
    ElasticHelper elasticHelper = new ElasticHelper();

    @Scheduled(fixedRate = 10000)
    public void generateCrJrData() {
        JSONObject record = dataSimulator.generateCrJrRecord();
        elasticHelper.insertData("crjr", record.getString("id"), record.toString());
        elasticHelper.getCrJrData();
    }
}