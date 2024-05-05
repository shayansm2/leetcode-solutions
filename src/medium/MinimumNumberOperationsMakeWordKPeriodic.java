package medium;

import java.util.HashMap;

public class MinimumNumberOperationsMakeWordKPeriodic {
    public int minimumOperationsToMakeKPeriodic(String word, int k) {
        HashMap<String, Integer> hashmap = new HashMap<>();
        int maxSoFar = 0;
        for (int i = 0; i < word.length(); i += k) {
            String sub = word.substring(i, i + k);
            int value;
            if (hashmap.containsKey(sub)) {
                value = hashmap.get(sub) + 1;
            } else {
                value = 1;
            }
            hashmap.put(sub, value);
            maxSoFar = Math.max(maxSoFar, value);
        }

        return (word.length() / k) - maxSoFar;
    }
}
