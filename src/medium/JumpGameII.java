package medium;

public class JumpGameII {
    public static void main(String[] args) {
        System.out.println(new JumpGameII().jump(new int[]{2, 3, 1, 1, 4}));
        System.out.println(new JumpGameII().jump(new int[]{2, 3, 0, 1, 4}));
    }

    public int jump(int[] nums) {
        int startIndex = 0;
        int endIndex = 0;
        int jumpCount = 0;
        while (endIndex < nums.length - 1) {
            jumpCount++;
            int start = startIndex;
            int end = endIndex;
            startIndex = endIndex + 1;
            for (int i = start; i <= end; i++) {
                endIndex = Math.max(endIndex, i + nums[i]);
                endIndex = Math.min(endIndex, nums.length - 1);
            }
        }
        return jumpCount;
    }
}
