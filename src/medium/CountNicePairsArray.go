package main

func countNicePairs(nums []int) int {
	counts := make(map[int]int)
	for _, num := range nums {
		val := num - rev(num)
		if _, found := counts[val]; found {
			counts[val]++
		} else {
			counts[val] = 1
		}
	}

	var result int

	for _, count := range counts {
		result += ((count * (count - 1)) / 2) % 1000000007
		result %= 1000000007
	}

	return result
}

func rev(number int) int {
	var revNumber int
	for number > 0 {
		digit := number % 10
		revNumber = 10*revNumber + digit
		number /= 10
	}
	return revNumber
}
