package main

import (
	"math"
)

func hammingWeight(num uint32) int {
	result := 0
	for num > 0 {
		base := math.Floor(math.Log2(float64(num)))
		num -= uint32(math.Pow(2, base))
		result++
	}
	return result
}
