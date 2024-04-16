public class MajorityElement {
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int counter = 0;
        for (int num : nums) {
            if (counter == 0) {
                candidate = num;
            }

            if (candidate == num) {
                counter++;
            } else {
                counter--;
            }
        }
        return candidate;
    }
}
