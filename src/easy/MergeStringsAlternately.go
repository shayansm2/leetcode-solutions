package main

import "fmt"

func main() {
	fmt.Println(mergeAlternately("abc", "pqr"))
	fmt.Println(mergeAlternately("ab", "pqrs"))
	fmt.Println(mergeAlternately("abcd", "pq"))
}

func mergeAlternately(word1 string, word2 string) string {
	i1, i2 := 0, 0
	var result string

	for i1 < len(word1) && i2 < len(word2) {
		if i1 == i2 {
			result += string(word1[i1])
			i1++
		} else {
			result += string(word2[i2])
			i2++
		}
	}

	if i1 < len(word1) {
		result += word1[i1:]
	}

	if i2 < len(word2) {
		result += word2[i2:]
	}

	return result
}
