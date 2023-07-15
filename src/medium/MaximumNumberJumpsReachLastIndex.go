package main

import "fmt"

func maximumJumps(nums []int, target int) int {
	maxJumps := make([]int, len(nums))

	for i := 0; i < len(nums)-1; i++ {
		maxJumps[i] = -1
	}

	for i := len(nums) - 2; i >= 0; i-- {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]-nums[j] > target || nums[j]-nums[i] > target {
				continue
			}

			if maxJumps[j] == -1 {
				continue
			}

			if maxJumps[i] < maxJumps[j]+1 {
				maxJumps[i] = maxJumps[j] + 1
			}
		}
	}

	fmt.Println(maxJumps)
	return maxJumps[0]
}

func main() {
	fmt.Println(maximumJumps([]int{1, 3, 6, 4, 1, 2}, 2)) //3
	fmt.Println(maximumJumps([]int{1, 3, 6, 4, 1, 2}, 1))
	fmt.Println(maximumJumps([]int{1, 3, 6, 4, 1, 2}, 3)) //5
	fmt.Println(maximumJumps([]int{1, 3, 6, 4, 1, 2}, 0)) //-1
}
