package main

func isGood(nums []int) bool {
	n := len(nums) - 1
	counter := make([]int, n+1)

	for _, num := range nums {
		if num > n || num < 1 {
			return false
		}

		if num == n {
			if counter[num] > 1 {
				return false
			}
		} else {
			if counter[num] > 0 {
				return false
			}
		}
		counter[num]++
	}

	return true
}
