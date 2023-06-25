package main

func numberOfGoodSubarraySplits(nums []int) int {
	prevIndex := -1
	const modulo = 1000000007
	result := 0
	for i, value := range nums {
		if value == 1 {
			if prevIndex == -1 {
				result = 1
			} else {
				result *= i - prevIndex
				result %= modulo
			}
			prevIndex = i
		}
	}
	return result
}
