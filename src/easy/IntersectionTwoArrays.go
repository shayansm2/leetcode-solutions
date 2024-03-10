package main

func intersection(nums1 []int, nums2 []int) []int {
	intersect := make(map[int]bool)

	for _, num := range nums1 {
		intersect[num] = false
	}

	for _, num := range nums2 {
		if _, found := intersect[num]; found {
			intersect[num] = true
		}
	}

	result := make([]int, 0)
	for num, val := range intersect {
		if val {
			result = append(result, num)
		}
	}
	return result
}
