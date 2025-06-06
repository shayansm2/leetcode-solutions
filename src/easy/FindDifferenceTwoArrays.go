package main

func findDifference(nums1 []int, nums2 []int) [][]int {
	map1 := make(map[int]bool)
	map2 := make(map[int]bool)
	for _, i := range nums1 {
		map1[i] = true
	}
	for _, i := range nums2 {
		map2[i] = true
	}

	res1 := make([]int, 0)
	res2 := make([]int, 0)
	for i := range map1 {
		if _, found := map2[i]; !found {
			res1 = append(res1, i)
		}
	}
	for i := range map2 {
		if _, found := map1[i]; !found {
			res2 = append(res2, i)
		}
	}
	return [][]int{res1, res2}
}
