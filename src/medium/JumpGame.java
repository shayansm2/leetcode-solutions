package medium;

public class JumpGame {
    public boolean canJump(int[] nums) {
        int lastIndex = 0;
        int index = 0;
        while (index <= lastIndex) {
            lastIndex = Math.max(index + nums[index], lastIndex);
            if (lastIndex >= nums.length - 1) {
                return true;
            }
            index++;
        }
        return false;
    }
}
