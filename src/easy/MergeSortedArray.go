package main

func merge(nums1 []int, m int, nums2 []int, n int) {
	index1 := m - 1
	index2 := n - 1
	resIndex := m + n - 1

	for resIndex >= 0 {
		if index1 >= 0 && (index2 < 0 || nums1[index1] > nums2[index2]) {
			nums1[resIndex] = nums1[index1]
			index1--
		} else if index2 >= 0 && (index1 < 0 || nums1[index1] <= nums2[index2]) {
			nums1[resIndex] = nums2[index2]
			index2--
		}

		resIndex--
	}
}
