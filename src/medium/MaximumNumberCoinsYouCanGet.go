package main

import "sort"

func maxCoins(piles []int) int {
	sort.Ints(piles)
	var result int
	for i := len(piles) / 3; i < len(piles); i += 2 {
		result += piles[i]
	}
	return result
}
