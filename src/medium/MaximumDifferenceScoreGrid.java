package medium;

import java.util.*;

public class MaximumDifferenceScoreGrid {
    public static void main(String[] args) {
        List<List<Integer>> matrix = new ArrayList<>();
        matrix.add(Arrays.asList(9, 5, 7, 3));
        matrix.add(Arrays.asList(8, 9, 6, 1));
        matrix.add(Arrays.asList(6, 7, 14, 3));
        matrix.add(Arrays.asList(2, 5, 3, 1));
        System.out.println(new MaximumDifferenceScoreGrid().maxScore(matrix));

        matrix = new ArrayList<>();
        matrix.add(Arrays.asList(4, 3, 2));
        matrix.add(Arrays.asList(3, 2, 1));
        System.out.println(new MaximumDifferenceScoreGrid().maxScore(matrix));
    }

    public int maxScore(List<List<Integer>> grid) {
        int columns = grid.getFirst().size();
        Integer result = null;
        List<List<Integer>> dp = new ArrayList<>();
        for (int i = 0; i < grid.size(); i++) {
            List<Integer> dpList = new ArrayList<>(columns);
            for (int j = 0; j < columns; j++) {
                // 0, 0
                if (i == 0 && j == 0) {
                    dpList.addLast(0);
                    continue;
                }
                // i, 0
                else if (j == 0) {
                    int move = grid.get(i).get(j) - grid.get(i - 1).get(j);
                    dpList.addLast(Math.max(move, dp.get(i - 1).get(j) + move));
                }
                // i, 0
                else if (i == 0) {
                    int move = grid.get(i).get(j) - grid.get(i).get(j - 1);
                    dpList.addLast(Math.max(move, dpList.get(j - 1) + move));
                }
                // i, j
                else {
                    int downMove = grid.get(i).get(j) - grid.get(i - 1).get(j);
                    int leftMove = grid.get(i).get(j) - grid.get(i).get(j - 1);
                    dpList.addLast(Math.max(
                            Math.max(downMove, dp.get(i - 1).get(j) + downMove),
                            Math.max(leftMove, dpList.get(j - 1) + leftMove)
                    ));
                }
//                System.out.println(new StringBuilder().append(i).append(" ").append(j).append(" :").append(dpList.get(j)));
                if (result == null) {
                    result = dpList.get(j);
                } else {
                    result = Math.max(result, dpList.get(j));
                }
            }
            dp.addLast(dpList);
        }
        return result;
    }
}
