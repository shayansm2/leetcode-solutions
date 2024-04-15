public class RemoveElement {
    public int removeElement(int[] nums, int val) {
        int tail = nums.length - 1;
        int current = 0;
        while (current <= tail) {
            if (nums[current] != val) {
                current++;
                continue;
            }

            int temp = nums[current];
            nums[current] = nums[tail];
            nums[tail] = temp;
            tail--;
        }
        return tail + 1;
    }
}
