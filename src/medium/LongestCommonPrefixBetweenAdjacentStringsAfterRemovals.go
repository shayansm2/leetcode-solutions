package main

import "fmt"

func commonPrefix(word1, word2 string) int {
	result := 0
	for result < min(len(word1), len(word2)) {
		if word1[result] == word2[result] {
			result++
		} else {
			return result
		}
	}
	return result
}

func longestCommonPrefix(words []string) []int {
	if len(words) <= 1 {
		return []int{0}
	}
	forward := make([]int, len(words))
	maxSoFar := 0
	for i := 1; i < len(words); i++ {
		maxSoFar = max(maxSoFar, commonPrefix(words[i], words[i-1]))
		forward[i] = maxSoFar
	}

	backward := make([]int, len(words))
	maxSoFar = 0
	for i := len(words) - 2; i >= 0; i-- {
		maxSoFar = max(maxSoFar, commonPrefix(words[i], words[i+1]))
		backward[i] = maxSoFar
	}

	// fmt.Println(forward)
	// fmt.Println(backward)

	result := make([]int, len(words))
	result[len(words)-1] = forward[len(words)-2]
	result[0] = backward[1]
	for i := 1; i < len(words)-1; i++ {
		// fmt.Println(i, forward[i-1], backward[i+1], commonPrefix(words[i-1], words[i+1]))
		result[i] = max(max(forward[i-1], backward[i+1]), commonPrefix(words[i-1], words[i+1]))
	}
	return result
}

func main() {
	fmt.Println(longestCommonPrefix([]string{"jump", "run", "run", "jump", "run"}))
	fmt.Println(longestCommonPrefix([]string{"dog", "racer", "car"}))
}
