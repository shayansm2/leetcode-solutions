public class MergeSortedArray {
    public static void main(String[] args) {
        MergeSortedArray solution = new MergeSortedArray();
        solution.merge(new int[]{1, 2, 3, 0, 0, 0}, 3, new int[]{2, 5, 6}, 3);
    }

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int pointer = m + n - 1;
        m--;
        n--;
        while (m >= 0 && n >= 0) {
            if (nums1[m] <= nums2[n]) {
                nums1[pointer] = nums2[n];
                n--;
            } else {
                nums1[pointer] = nums1[m];
                m--;
            }
            pointer--;
        }

        while (n >= 0) {
            nums1[pointer] = nums2[n];
            n--;
            pointer--;
        }
    }
}
