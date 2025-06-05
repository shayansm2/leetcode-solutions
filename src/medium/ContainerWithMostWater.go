package main

import "fmt"

func findMinGreaterEqualThan(nums []int, target int) int {
	s, e := 0, len(nums)-1
	for s <= e {
		m := (s + e) / 2
		if nums[m] == target {
			return m
		}
		if nums[m] < target {
			s = m + 1
		} else {
			e = m - 1
		}
	}
	return s
}

func maxArea(height []int) int {
	forwardMaxVal := make([]int, 0)
	forwardMaxIndex := make([]int, 0)
	forwardMax := 0
	for i, val := range height {
		if forwardMax < val {
			forwardMax = val
			forwardMaxVal = append(forwardMaxVal, val)
			forwardMaxIndex = append(forwardMaxIndex, i)
		}
	}

	backwardMaxVal := make([]int, 0)
	backwardMaxIndex := make([]int, 0)
	backwardMax := 0
	for i := len(height) - 1; i >= 0; i-- {
		val := height[i]
		if backwardMax < val {
			backwardMax = val
			backwardMaxVal = append(backwardMaxVal, val)
			backwardMaxIndex = append(backwardMaxIndex, i)
		}
	}

	result := 0
	for i, val := range height {
		fi := forwardMaxIndex[findMinGreaterEqualThan(forwardMaxVal, val)]
		bi := backwardMaxIndex[findMinGreaterEqualThan(backwardMaxVal, val)]
		maxLen := i - fi
		if bi-i > maxLen {
			maxLen = bi - i
		}
		fmt.Println(i, maxLen)
		if result < maxLen*val {
			result = maxLen * val
		}
	}

	return result
}

func main() {
	fmt.Println(maxArea([]int{1, 8, 6, 2, 5, 4, 8, 3, 7}))
}
