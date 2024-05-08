import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;

public class RelativeRanks {
    public String[] findRelativeRanks(int[] score) {
        Integer[] scores = Arrays.stream(score).boxed().toArray(Integer[]::new);
        Arrays.sort(scores, Collections.reverseOrder());
        HashMap<Integer, Integer> score2position = new HashMap<>();
        for (int i = 0; i < scores.length; i++) {
            score2position.put(scores[i], i + 1);
        }

        String[] result = new String[score.length];
        for (int i = 0; i < score.length; i++) {
            int position = score2position.get(score[i]);
            if (position == 1) {
                result[i] = "Gold Medal";
            } else if (position == 2) {
                result[i] = "Silver Medal";
            } else if (position == 3) {
                result[i] = "Bronze Medal";
            } else {
                result[i] = String.valueOf(position);
            }
        }
        return result;
    }
}
