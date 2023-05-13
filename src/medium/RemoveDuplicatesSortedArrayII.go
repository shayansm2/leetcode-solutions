package main

// pretty similar to RemoveDuplicatesSortedArray.go
func removeDuplicates(nums []int) int {
	if len(nums) < 3 {
		return len(nums)
	}

	slow := 0
	for fast := 2; fast < len(nums); fast++ {
		if nums[fast] > nums[slow] {
			nums[slow+2] = nums[fast]
			slow++
		}
	}
	return slow + 2
}
