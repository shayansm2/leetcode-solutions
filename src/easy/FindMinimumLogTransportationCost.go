package main

func minCuttingCost(n int, m int, k int) int64 {
	var result int64 = 0
	if m > k {
		result += int64((m - k) * k)
	}
	if n > k {
		result += int64((n - k) * k)
	}
	return result
}
