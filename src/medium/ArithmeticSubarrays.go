package main

import (
	"sort"
)

func checkArithmeticSubarrays(nums []int, l []int, r []int) []bool {
	result := make([]bool, len(l))
	for i := 0; i < len(l); i++ {
		left, right := l[i], r[i]
		subArray := make([]int, right-left+1)
		copy(subArray, nums[left:right+1])
		result[i] = betterIsArithmetic(subArray)
	}
	return result
}

func betterIsArithmetic(array []int) bool {
	maximum, minimum := array[0], array[0]
	hashMap := make(map[int]bool)
	for _, number := range array {
		maximum = max(maximum, number)
		minimum = min(minimum, number)
		hashMap[number] = true
	}

	if (maximum-minimum)%(len(array)-1) != 0 {
		return false
	}

	dif := (maximum - minimum) / (len(array) - 1)
	current := minimum + dif

	for current < maximum {
		if _, found := hashMap[current]; !found {
			return false
		}
		current += dif
	}
	return true
}

func isArithmetic(array []int) bool {
	sort.Ints(array)
	dif := array[1] - array[0]
	for i := 1; i < len(array)-1; i++ {
		if array[i+1]-array[i] != dif {
			return false
		}
	}
	return true
}
