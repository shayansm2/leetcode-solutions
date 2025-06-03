package main

import (
	"fmt"
	"strings"
)

func isVowel(char string) bool {
	vowles := "aeiouAEIOU"
	for _, vowel := range vowles {
		if string(vowel) == char {
			return true
		}
	}
	return false
}

func reverseVowels(s string) string {
	vowelIndices := make([]int, 0)
	for i, char := range s {
		if isVowel(string(char)) {
			vowelIndices = append(vowelIndices, i)
		}
	}
	result := strings.Split(s, "")
	fmt.Println(result)
	for i, index := range vowelIndices {
		result[index] = string(s[vowelIndices[len(vowelIndices)-i-1]])
	}
	return strings.Join(result, "")
}
