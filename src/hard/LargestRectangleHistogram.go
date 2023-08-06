package main

import "fmt"

func largestRectangleArea(heights []int) int {
	prevMinIndex, nextMinIndex := make([]int, len(heights)), make([]int, len(heights))
	for i := range heights {
		prevMinIndex[i], nextMinIndex[i] = -1, -1
	}

	type element struct {
		index int
		value int
	}

	var stack []element
	for i, height := range heights {
		for len(stack) > 0 && stack[len(stack)-1].value > height {
			lastElement := stack[len(stack)-1]
			nextMinIndex[lastElement.index] = i
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, element{i, height})
	}

	stack = []element{}
	for i := len(heights) - 1; i >= 0; i-- {
		height := heights[i]
		for len(stack) > 0 && stack[len(stack)-1].value > height {
			lastElement := stack[len(stack)-1]
			prevMinIndex[lastElement.index] = i
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, element{i, height})
	}

	maxArea := 0
	for i, height := range heights {
		startIndex := prevMinIndex[i] + 1
		endIndex := nextMinIndex[i] - 1
		if endIndex < 0 {
			endIndex = len(heights) - 1
		}

		length := endIndex - startIndex + 1

		if maxArea < length*height {
			maxArea = length * height
		}
	}
	return maxArea
}

func main() {
	fmt.Println(largestRectangleArea([]int{2, 1, 5, 6, 2, 3}))
}
