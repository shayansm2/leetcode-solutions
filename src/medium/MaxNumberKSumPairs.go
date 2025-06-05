package main

import "slices"

func maxOperations(nums []int, k int) int {
	slices.Sort(nums)
	start := 0
	end := len(nums) - 1
	result := 0
	for start < end {
		sum := nums[start] + nums[end]
		if sum == k {
			start++
			end--
			result++
		} else if sum < k {
			start++
		} else {
			end--
		}
	}
	return result
}
