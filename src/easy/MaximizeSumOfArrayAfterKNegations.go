package main

import (
	"sort"
)

func largestSumAfterKNegations(nums []int, k int) int {
	sort.Ints(nums)

	sum := 0
	for _, num := range nums {
		sum += num
	}

	flipIndex := 0
	for k > 0 && flipIndex < len(nums) && nums[flipIndex] < 0 {
		sum += -2 * nums[flipIndex]
		flipIndex++
		k--
	}

	if k > 0 && k%2 == 1 {
		// get the min index
		minIndex := flipIndex
		if flipIndex == len(nums) {
			minIndex--
		} else if flipIndex > 0 && nums[flipIndex] > -nums[flipIndex-1] {
			minIndex--
		}

		if nums[minIndex] > 0 {
			sum -= 2 * nums[minIndex]
		} else {
			sum += 2 * nums[minIndex]
		}
	}

	return sum
}
