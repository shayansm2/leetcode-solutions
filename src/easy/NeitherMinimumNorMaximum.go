package main

func findNonMinOrMax(nums []int) int {
	min, max := nums[0], nums[0]

	for i := 1; i < len(nums); i++ {
		if nums[i] < min {
			min = nums[i]
		}

		if nums[i] > max {
			max = nums[i]
		}
	}

	for i := 0; i < len(nums); i++ {
		if nums[i] != max && nums[i] != min {
			return nums[i]
		}
	}

	return -1
}
