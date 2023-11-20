package main

import "sort"

func reductionOperations(nums []int) int {
	counts := make(map[int]int)
	var distinct []int

	for _, num := range nums {
		if _, found := counts[num]; found {
			counts[num]++
		} else {
			counts[num] = 1
			distinct = append(distinct, num)
		}
	}

	sort.Ints(distinct)

	result := 0

	for index, num := range distinct {
		result += index * counts[num]
	}

	return result
}
