import java.util.HashMap;

public class PermutationDifferenceTwoStrings {
    public int findPermutationDifference(String s, String t) {
        HashMap<Character, Integer> sMap = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            sMap.put(s.charAt(i), i);
        }

        int result = 0;
        for (int i = 0; i < t.length(); i++) {
            int j = sMap.get(t.charAt(i));
            result += Math.max(i - j, j - i);
        }

        return result;
    }
}
