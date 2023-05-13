package main

import (
	"fmt"
)

func majorityElement(nums []int) int {
	hashTable := make(map[int]int)

	for _, i := range nums {
		hashTable[i]++
	}

	for element, majority := range hashTable {
		if majority > len(nums)/2 {
			return element
		}
	}

	return 1
}

func main() {
	fmt.Println(majorityElement([]int{3, 2, 3}))
	fmt.Println(majorityElement([]int{2, 2, 1, 1, 1, 2, 2}))
}
