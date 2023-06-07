package main

import (
	"fmt"
	"math"
	"strconv"
)

func minFlips(a int, b int, c int) int {
	A := strconv.FormatInt(int64(a), 2)
	B := strconv.FormatInt(int64(b), 2)
	C := strconv.FormatInt(int64(c), 2)
	counter := 0
	for i := 1; i <= int(math.Max(float64(len(A)), math.Max(float64(len(B)), float64(len(C))))); i++ {
		x, y, z := getIthDigit(A, i), getIthDigit(B, i), getIthDigit(C, i)
		if (x || y) == z {
			continue
		}

		if z {
			counter++
		} else {
			if x {
				counter++
			}
			if y {
				counter++
			}
		}
	}
	return counter
}

func getIthDigit(number string, i int) bool {
	if i > len(number) {
		return false
	}

	if string(number[len(number)-i]) == "0" {
		return false
	}

	return true
}

func main() {
	fmt.Println(minFlips(2, 6, 5))
	fmt.Println(minFlips(4, 2, 7))
	fmt.Println(minFlips(1, 2, 3))
}
