package main

import "strconv"

func largestOddNumber(num string) string {
	lastIndex := len(num) - 1
	for lastIndex >= 0 {
		lastDigit, _ := strconv.Atoi(string(num[lastIndex]))
		if lastDigit%2 == 1 {
			break
		}
		lastIndex--
	}
	return num[0 : lastIndex+1]
}
