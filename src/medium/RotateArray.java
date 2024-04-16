package medium;

public class RotateArray {
    public void rotate(int[] nums, int k) {
        for (int i = 0; i < gcd(nums.length, k); i++) {
            int index = i;
            int num = nums[index];
            do {
                index = (index + k) % nums.length;
                int temp = nums[index];
                nums[index] = num;
                num = temp;
            } while (index != i);
        }
    }

    public static int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
}
