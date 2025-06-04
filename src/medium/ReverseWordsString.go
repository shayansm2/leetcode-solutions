package main

import "strings"

func reverseWords(s string) string {
	words := make([]string, 0)
	startIndex := -1
	for i, char := range s {
		if startIndex >= 0 && string(char) == " " {
			words = append([]string{string(s[startIndex:i])}, words...)
			startIndex = -1
		}
		if startIndex == -1 && string(char) != " " {
			startIndex = i
		}
	}
	if startIndex >= 0 {
		words = append([]string{string(s[startIndex:len(s)])}, words...)
	}
	return strings.Join(words, " ")
}
