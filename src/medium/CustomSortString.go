package main

import "strings"

func customSortString(order string, s string) string {
	counts := make(map[rune]int)
	for _, char := range s {
		if _, found := counts[char]; found {
			counts[char]++
		} else {
			counts[char] = 1
		}
	}

	result := ""

	for _, char := range order {
		if count, found := counts[char]; found {
			result += strings.Repeat(string(char), count)
			delete(counts, char)
		}
	}

	for char, count := range counts {
		result += strings.Repeat(string(char), count)
	}

	return result
}
