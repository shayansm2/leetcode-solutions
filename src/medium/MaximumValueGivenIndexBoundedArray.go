package main

import "fmt"

func maxValue(n int, index int, maxSum int) int {
	min := maxSum / n
	max := maxSum

	for min <= max {
		mid := min + (max-min)/2

		val := getMinSum(n, index, mid)

		if val <= maxSum && getMinSum(n, index, mid+1) > maxSum {
			return mid
		}

		if val > maxSum {
			max = mid - 1
		} else {
			min = mid + 1
		}
	}

	return -1
}

func getMinSum(n int, i int, x int) int {
	beforeIndexSum, afterIndexSum := 0, 0
	if i > x-2 {
		beforeIndexSum = (x - 1) * (x - 2) / 2
	} else {
		beforeIndexSum = (2*x - i - 3) * i / 2
	}

	if x < n-i+1 {
		afterIndexSum = (x - 1) * (x - 2) / 2
	} else {
		afterIndexSum = (2*x - n + i - 2) * (n - i - 1) / 2
	}

	return x - 1 + n + beforeIndexSum + afterIndexSum
}

func main() {
	fmt.Println(maxValue(4, 2, 6))  // 2
	fmt.Println(maxValue(6, 1, 10)) // 3
	fmt.Println(maxValue(8, 7, 14)) // 4
	fmt.Println(maxValue(9, 3, 16)) // 3
}
