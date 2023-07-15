package main

import "fmt"

func checkArray(nums []int, k int) bool {
	nonZeroIndex := -1
	decreaseStep := 0

	for i, val := range nums {
		if val == 0 {
			if nonZeroIndex != -1 && i < nonZeroIndex+k {
				return false
			}

			continue
		}

		if nonZeroIndex == -1 {
			nonZeroIndex = i
			decreaseStep = nums[i]
		}

		if nonZeroIndex != -1 && i < nonZeroIndex+k && decreaseStep > nums[i] {
			decreaseStep = nums[i]
		}
	}

	if nonZeroIndex == -1 {
		return true
	}

	if nonZeroIndex+k > len(nums) {
		return false
	}

	for i := 0; i < k; i++ {
		nums[nonZeroIndex+i] -= decreaseStep
	}

	return checkArray(nums, k)
}

func main() {
	fmt.Println(checkArray([]int{2, 2, 3, 1, 1, 0}, 3))
	fmt.Println(checkArray([]int{1, 3, 1, 1}, 2))
	fmt.Println(checkArray([]int{0, 45, 82, 98, 99}, 4))
	fmt.Println(checkArray([]int{60, 72, 87, 89, 63, 52, 64, 62, 31, 37, 57, 83, 98, 94, 92, 77, 94, 91, 87, 100, 91, 91, 50, 26}, 4))
}
