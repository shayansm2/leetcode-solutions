package main

import "slices"

func getSortedCharCount(word string) ([]int, map[rune]int) {
	m := make(map[rune]int)
	for _, c := range word {
		m[c] = m[c] + 1
	}
	res := make([]int, len(m))
	i := 0
	for _, v := range m {
		res[i] = v
		i++
	}
	slices.Sort(res)
	return res, m
}
func closeStrings(word1 string, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	}

	count1, chars1 := getSortedCharCount(word1)
	count2, chars2 := getSortedCharCount(word2)
	if !slices.Equal(count1, count2) {
		return false
	}
	for char := range chars1 {
		if _, found := chars2[char]; !found {
			return false
		}
	}
	return true
}
