package main

import (
	"fmt"
	"math"
	"strconv"
)

func makeTheIntegerZero(num1 int, num2 int) int {
	if num1 == 0 {
		return 0
	}

	counter := 0

	for num1 > 0 && num1 < int(math.Pow(2, 60)) {
		num1 -= num2
		counter++

		if num1 < 0 {
			break
		}

		if countOnes(num1) <= counter && num1 >= counter {
			return counter
		}
	}

	return -1
}

func countOnes(n int) int {
	// Convert the integer to binary string
	binaryStr := strconv.FormatInt(int64(n), 2)

	// Count the number of ones in the binary string
	count := 0
	for _, char := range binaryStr {
		if char == '1' {
			count++
		}
	}

	return count
}

func main() {
	fmt.Println(makeTheIntegerZero(3, -2))
	fmt.Println(makeTheIntegerZero(5, 7))
	fmt.Println(makeTheIntegerZero(110, 55))
}
