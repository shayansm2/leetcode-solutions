package main

import "fmt"

func semiOrderedPermutation(nums []int) int {
	var firstIndex, lastIndex int
	for i, val := range nums {
		if val == 1 {
			firstIndex = i
		} else if val == len(nums) {
			lastIndex = i
		}
	}

	if firstIndex > lastIndex {
		return firstIndex + len(nums) - lastIndex - 2
	}
	return firstIndex + len(nums) - lastIndex - 1
}

func main() {
	fmt.Println(semiOrderedPermutation([]int{2, 1, 4, 3}))
	fmt.Println(semiOrderedPermutation([]int{2, 4, 1, 3}))
	fmt.Println(semiOrderedPermutation([]int{1, 3, 4, 2, 5}))
}
