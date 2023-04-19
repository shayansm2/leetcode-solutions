package main

import "fmt"

func main() {
	fmt.Println(pivotIndex([]int{1, 7, 3, 6, 5, 6}))
	fmt.Println(pivotIndex([]int{1, 2, 3}))
	fmt.Println(pivotIndex([]int{2, 1, -1}))
}

func pivotIndex(nums []int) int {
	var cumsum []int
	var sum int
	for _, num := range nums {
		sum += num
		cumsum = append(cumsum, sum)
	}

	if sum-nums[0] == 0 {
		return 0
	}

	for i := 1; i < len(cumsum)-1; i++ {
		if cumsum[i-1] == cumsum[len(cumsum)-1]-cumsum[i] {
			return i
		}
	}

	if sum-nums[len(nums)-1] == 0 {
		return len(nums) - 1
	}

	return -1
}
