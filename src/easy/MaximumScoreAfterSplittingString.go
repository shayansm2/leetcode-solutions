package main

import "fmt"

func maxScore(s string) int {
	scores := make([]int, len(s)-1)
	var counter int
	for i := 0; i < len(s)-1; i++ {
		if string(s[i]) == "0" {
			counter++
		}
		scores[i] += counter
	}

	counter = 0
	for i := len(s) - 1; i > 0; i-- {
		if string(s[i]) == "1" {
			counter++
		}
		scores[i-1] += counter
	}

	fmt.Println(scores)

	var result int
	for _, score := range scores {
		if result < score {
			result = score
		}
	}
	return result
}
