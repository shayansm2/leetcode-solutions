package main

import "fmt"

func nextGreaterElement(nums1 []int, nums2 []int) []int {
	nextGraterElementIndices := make(map[int]int)
	for _, val := range nums2 {
		nextGraterElementIndices[val] = -1
	}

	var descStack []int

	for _, val := range nums2 {
		for len(descStack) > 0 && descStack[len(descStack)-1] < val {
			nextGraterElementIndices[descStack[len(descStack)-1]] = val
			descStack = descStack[:len(descStack)-1]
		}
		descStack = append(descStack, val)
	}

	result := make([]int, len(nums1))
	for i, val := range nums1 {
		result[i] = nextGraterElementIndices[val]
	}

	return result
}

func main() {
	fmt.Println(nextGreaterElement([]int{4, 1, 2}, []int{1, 3, 4, 2}), []int{-1, 3, -1})
}
