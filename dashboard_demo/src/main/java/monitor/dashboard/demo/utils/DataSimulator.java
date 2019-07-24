package monitor.dashboard.demo.utils;

import org.apache.commons.codec.digest.DigestUtils;
import org.json.JSONObject;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class DataSimulator {

    List<String> crList = new ArrayList<>();
    List<String> jrList = new ArrayList<>();
    List<String> jrstatus = new ArrayList<>();
    Random random = new Random();

    public DataSimulator() {
        crList = IntStream.range(1, 100).boxed().map(x -> String.format("cr%s", x)).collect(Collectors.toList());
        jrList = IntStream.range(1, 100).boxed().map(x -> String.format("jr%s", x)).collect(Collectors.toList());
        jrstatus = IntStream.range(1,5).boxed().map(x->x.toString()).collect(Collectors.toList());
    }

    public String getRandomCr() {
        int id = random.nextInt(crList.size());
        return crList.get(id);
    }

    public String getRandomJr() {
        int id = random.nextInt(jrList.size());
        return jrList.get(id);
    }

    public String getRandomJrStatus() {
        int id = random.nextInt(jrstatus.size());
        return jrstatus.get(id);
    }

    public JSONObject generateCrJrRecord() {
        JSONObject record = new JSONObject();
        String cr = getRandomCr();
        String jr = getRandomJr();
        String status = getRandomJrStatus();
        LocalDateTime current = LocalDateTime.now();
        LocalDateTime crStart = current.plusHours(random.nextInt(3));
        LocalDateTime crEnd = crStart.plusHours(random.nextInt(24 - crStart.getHour()));

        String timestamp = current.toString();

        record.put("cr", cr);
        record.put("cr_start", crStart.toString());
        record.put("cr_end", crEnd.toString());

        record.put("jr", jr);
        record.put("jr_status", status);
        record.put("@timestamp", timestamp);

        LocalDateTime.now().plusHours(5);

        String combine = String.join("|", cr, crStart.toString(), crEnd.toString(), jr, status, timestamp);
        String id = DigestUtils.sha1Hex(combine);
        record.put("id", id);
        return record;
    }
}
