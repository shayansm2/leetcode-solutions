package main

func productExceptSelf(nums []int) []int {
	result := make([]int, len(nums))
	for i := range result {
		result[i] = 1
	}

	for i := 1; i < len(nums); i++ {
		result[i] = nums[i-1] * result[i-1]
	}

	multiply := 1
	for i := len(nums) - 2; i >= 0; i-- {
		multiply *= nums[i+1]
		result[i] *= multiply
	}

	return result
}
