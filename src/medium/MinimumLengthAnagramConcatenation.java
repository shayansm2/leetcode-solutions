package medium;

import java.util.Arrays;
import java.util.HashMap;

public class MinimumLengthAnagramConcatenation {
    public static void main(String[] args) {
        System.out.println(new MinimumLengthAnagramConcatenation().minAnagramLength("lbuorourlb"));
    }

    public int minAnagramLength(String s) {
        HashMap<Character, Integer> charCount = new HashMap<>();
        for (char i : s.toCharArray()) {
            charCount.put(i, charCount.getOrDefault(i, 0) + 1);
        }

        int minRepeat = s.length();
        for (Integer i : charCount.values()) {
            minRepeat = Math.min(i, minRepeat);
        }

        for (int k = s.length() / minRepeat; k < s.length(); k++) {
            if (s.length() % k != 0) {
                continue;
            }

            if (isAnagram(s, k)) {
                return k;
            }
        }
        return s.length();
    }

    private boolean isAnagram(String s, int len) {
        String template = getSort(s.substring(0, len));

        for (int j = 1; j < s.length() / len; j++) {
            String sub = getSort(s.substring(j * len, (j + 1) * len));

            if (!sub.equals(template)) {
                return false;
            }
        }
        return true;
    }

    private static String getSort(String original) {
        char[] chars = original.toCharArray();
        Arrays.sort(chars);
        return new String(chars);
    }
}
