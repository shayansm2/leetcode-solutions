package main

import (
	"fmt"
	"strconv"
)

func removeKdigits(num string, k int) string {
	if len(num) == k {
		return "0"
	}

	var stack string
	for _, char := range num {
		number, _ := strconv.Atoi(string(char))
		for len(stack) > 0 && k > 0 {
			lastNumber, _ := strconv.Atoi(string(stack[len(stack)-1]))
			if lastNumber >= number {
				k--
				stack = stack[:len(stack)-1]
			} else {
				break
			}
		}
		if string(char) == "0" && len(stack) == 0 {
			continue
		}
		stack += string(char)
	}

	if len(stack) <= k {
		return "0"
	}

	stack = stack[:len(stack)-k]

	if len(stack) == 0 {
		return "0"
	}

	return stack
}

func main() {
	fmt.Println(removeKdigits("1432219", 3))
	fmt.Println(removeKdigits("10200", 1))
}
