package main

import "fmt"

func longestSubarray(nums []int) int {
	start := 0
	end := -1
	zeroCount := 0
	oneCount := 0
	result := 0

	for end < len(nums)-1 {
		if zeroCount <= 1 {
			result = max(result, oneCount+zeroCount-1)
			end++
			if nums[end] == 1 {
				oneCount++
			} else {
				zeroCount++
			}
		} else {
			if nums[start] == 1 {
				oneCount--
			} else {
				zeroCount--
			}
			start++
		}
		fmt.Println(start, end, nums[start:end+1], "1:", oneCount, "0:", zeroCount)
	}
	if zeroCount <= 1 {
		result = max(result, oneCount+zeroCount-1)
	}
	return result
}
