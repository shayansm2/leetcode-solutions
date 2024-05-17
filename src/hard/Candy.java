package hard;

import java.util.Arrays;

public class Candy {
    public int candy(int[] ratings) {
        int[] candies = new int[ratings.length];
        int candy = 0;
        for (int i = 1; i < ratings.length; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candy++;
            } else {
                candy = 0;
            }
            candies[i] = Math.max(candies[i], candy);
        }
        candy = 0;
        for (int i = ratings.length - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                candy++;
            } else {
                candy = 0;
            }
            candies[i] = Math.max(candies[i], candy);
        }
        return Arrays.stream(candies).sum() + candies.length;
    }
}
