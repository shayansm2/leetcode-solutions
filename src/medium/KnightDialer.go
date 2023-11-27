package main

func knightDialer(n int) int {
	modulo := 1000000007
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, 10)
		if i == 0 {
			dp[i] = []int{1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
			continue
		}

		for digit := 0; digit < 10; digit++ {
			for _, nextDigit := range getKnightMovements(digit) {
				dp[i][digit] += dp[i-1][nextDigit] % modulo
				dp[i][digit] %= modulo
			}
		}
	}
	result := 0
	for digit := 0; digit < 10; digit++ {
		result += dp[n-1][digit] % modulo
		result %= modulo
	}
	return result
}

func getKnightMovements(digit int) []int {
	switch digit {
	case 0:
		return []int{4, 6}
	case 1:
		return []int{6, 8}
	case 2:
		return []int{7, 9}
	case 3:
		return []int{4, 8}
	case 4:
		return []int{0, 3, 9}
	case 5:
		return []int{}
	case 6:
		return []int{0, 1, 7}
	case 7:
		return []int{2, 6}
	case 8:
		return []int{1, 3}
	case 9:
		return []int{2, 4}
	}
	return []int{}
}

func main() {
	print(knightDialer(3131))
}
