package medium;

import java.util.HashMap;

public class SumDigitDifferencesAllPairs {
    public static void main(String[] args) {
        System.out.println(
                new SumDigitDifferencesAllPairs().sumDigitDifferences(new int[]{10, 10, 10, 10})
        );
    }
    public long sumDigitDifferences(int[] nums) {
        int numberOfDigits = String.valueOf(nums[0]).length();
        long result = 0;
        for (int digitIndex = 0; digitIndex < numberOfDigits; digitIndex++) {
            HashMap<Character, Integer> counts = new HashMap<>();
            for (int num : nums) {
                char digit = String.valueOf(num).charAt(digitIndex);
                counts.put(digit, counts.getOrDefault(digit, 0) + 1);
            }

            long diffs = 0;
            Integer[] values = counts.values().toArray(new Integer[0]);
            for (int i = 0; i < values.length - 1; i++) {
                for (int j = i + 1; j < values.length; j++) {
                    diffs += (long) values[i] * values[j];
                }
            }

            result += diffs;
        }
        return result;
    }
}
