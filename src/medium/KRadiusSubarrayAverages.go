package main

import "fmt"

func getAverages(nums []int, k int) []int {
	result := make([]int, len(nums))
	for i := range result {
		result[i] = -1
	}

	var sum int
	for lastIndex, val := range nums {
		curIndex := lastIndex - k
		sum += val
		if curIndex < k || curIndex >= len(nums)-k {
			continue
		}
		result[curIndex] = sum / (2*k + 1)
		sum -= nums[curIndex-k]
	}

	return result
}

func main() {
	fmt.Println(getAverages([]int{7, 4, 3, 9, 1, 8, 5, 2, 6}, 3))
}
