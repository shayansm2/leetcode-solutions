package medium;

public class RemoveDuplicatesSortedArrayII {
    public int removeDuplicates(int[] nums) {
        int currentValue = nums[0];
        int count = 1;
        int pointer = 1;

        for (int i = 1; i < nums.length; i++) {
            /**
             * num_i < cur_val & count = 1 -> continue
             * num_i < cur_val & count = 2 -> continue
             * num_i = cur_val & count = 1 -> set cur_value & counter ++
             * num_i = cur_val & count = 2 -> continue
             * num_i > cur_val & count = 1 -> set cur_value
             * num_i > cur_val & count = 2 -> set cur_value
             */
            if (nums[i] > currentValue) {
                nums[pointer] = nums[i];
                currentValue = nums[i];
                pointer++;
                count = 1;
            } else if (nums[i] == currentValue && count == 1) {
                nums[pointer] = nums[i];
                currentValue = nums[i];
                count++;
                pointer++;
            }
        }
        return pointer;
    }
}
