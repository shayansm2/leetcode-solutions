package main

import "fmt"

func alternatingSubarray(nums []int) int {
	startIndex := 0
	longestLen := -1
	for curIndex := 1; curIndex < len(nums); curIndex++ {
		if isAlternating(startIndex, curIndex, nums) {
			longestLen = max(longestLen, curIndex-startIndex+1)
		} else {
			if isAlternating(curIndex-1, curIndex, nums) {
				startIndex = curIndex - 1
			} else {
				startIndex = curIndex
			}
		}
	}
	return longestLen
}

func isAlternating(startIndex int, curIndex int, nums []int) bool {
	if startIndex%2 == curIndex%2 {
		return nums[startIndex] == nums[curIndex]
	}
	return nums[startIndex]+1 == nums[curIndex]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(alternatingSubarray([]int{2, 3, 4, 3, 4}))
}
