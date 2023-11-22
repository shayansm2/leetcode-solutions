package main

import "sort"

func findDiagonalOrder(nums [][]int) []int {
	var keys []int
	hashMap := make(map[int][]int)
	for i, row := range nums {
		for j, num := range row {
			key := i + j
			if _, found := hashMap[key]; found {
				hashMap[key] = append(hashMap[key], num)
			} else {
				hashMap[key] = []int{num}
				keys = append(keys, key)
			}
		}
	}

	sort.Ints(keys)

	var result []int
	for _, key := range keys {
		vals := hashMap[key]

		for i, j := 0, len(vals)-1; i < j; i, j = i+1, j-1 {
			vals[i], vals[j] = vals[j], vals[i]
		}

		result = append(result, vals...)
	}

	return result
}
