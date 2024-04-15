public class RemoveDuplicatesSortedArray {
    public int removeDuplicates(int[] nums) {
        int pointer = 1;
        int currentValue = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > currentValue) {
                nums[pointer] = nums[i];
                pointer++;
                currentValue = nums[i];
            }
        }

        return pointer;
    }
}
