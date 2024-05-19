package medium;

import java.util.ArrayList;
import java.util.Arrays;

public class SpecialArrayII {
    public static void main(String[] args) {
        System.out.println(
                Arrays.toString(new SpecialArrayII().isArraySpecial(
                        new int[]{3, 4, 1, 2, 6}, new int[][]{{0, 4}}
                ))
        );
    }

    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        boolean[] result = new boolean[queries.length];
        if (nums.length < 2) {
            Arrays.fill(result, true);
            return result;
        }

        ArrayList<Integer> specialArraysFirstIndex = new ArrayList<>();
        specialArraysFirstIndex.addFirst(0);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] % 2 == nums[i - 1] % 2) {
                specialArraysFirstIndex.addLast(i);
            }
        }

        System.out.println(specialArraysFirstIndex);

        for (int i = 0; i < queries.length; i++) {
            int start = queries[i][0];
            int end = queries[i][1];
            int index = findHighestValueLowerOrEqual(specialArraysFirstIndex, start);
            boolean res = specialArraysFirstIndex.get(index) <= start;
            if (index < specialArraysFirstIndex.size() - 1) {
                res = res && specialArraysFirstIndex.get(index + 1) > end;
            }
            result[i] = res;
        }
        return result;
    }

    private static int findHighestValueLowerOrEqual(ArrayList<Integer> arr, int input) {
        int low = 0;
        int high = arr.size() - 1;
        int resultIndex = -1;
        int resultValue = Integer.MIN_VALUE;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (arr.get(mid) <= input) {
                if (arr.get(mid) > resultValue) {
                    resultValue = arr.get(mid);
                    resultIndex = mid;
                }
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return resultIndex;
    }
}
