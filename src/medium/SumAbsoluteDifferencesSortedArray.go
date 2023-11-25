package main

func getSumAbsoluteDifferences(nums []int) []int {
	n := len(nums)
	cumSum := make([]int, n)
	sum := 0
	for i, num := range nums {
		sum += num
		cumSum[i] = sum
	}

	result := make([]int, n)
	for i, num := range nums {
		result[i] = (2*i - n) * num
		result[i] += cumSum[n-1]
		if i > 0 {
			result[i] -= 2 * cumSum[i-1]
		}
	}
	return result
}
