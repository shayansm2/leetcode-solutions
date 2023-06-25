package main

func countBeautifulPairs(nums []int) int {
	counter := 0
	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if gcd(firstDigit(nums[i]), lastDigit(nums[j])) == 1 {
				counter++
			}
		}
	}
	return counter
}

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func firstDigit(number int) int {
	for number >= 10 {
		number /= 10
	}
	return number
}

func lastDigit(number int) int {
	return number % 10
}
