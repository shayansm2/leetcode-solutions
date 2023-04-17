package main

import (
	"fmt"
)

func main() {
	fmt.Println(kidsWithCandies([]int{2, 3, 5, 1, 3}, 3))
	fmt.Println(kidsWithCandies([]int{4, 2, 1, 1, 2}, 1))
	fmt.Println(kidsWithCandies([]int{12, 1, 12}, 10))
}

func kidsWithCandies(candies []int, extraCandies int) []bool {
	maxVal := 0

	for _, candie := range candies {
		if candie > maxVal {
			maxVal = candie
		}
	}

	var result = make([]bool, len(candies))
	for i, candie := range candies {
		if candie+extraCandies >= maxVal {
			result[i] = true
		}
	}

	return result
}
