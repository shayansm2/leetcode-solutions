public class FindIntegerAddedArrayI {
    public int addedInteger(int[] nums1, int[] nums2) {
        int min1, min2;
        min1 = nums1[0];
        min2 = nums2[0];
        for (int num :nums1) {
            if (min1 < num) {
                min1 = num;
            }
        }
        for (int num :nums2) {
            if (min2 < num) {
                min2 = num;
            }
        }
        return min2 - min1;
    }
}
