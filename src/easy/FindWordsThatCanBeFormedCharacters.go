package main

func countCharacters(words []string, chars string) int {
	dict := make(map[int32]int)

	for _, char := range chars {
		if _, found := dict[char]; found {
			dict[char]++
		} else {
			dict[char] = 1
		}
	}

	var result int
	for _, word := range words {
		copyDict := copyMap(dict)
		if canBeFormed(word, copyDict) {
			result += len(word)
		}
	}
	return result
}

func canBeFormed(word string, copyDict map[int32]int) bool {
	for _, char := range word {
		if val, found := copyDict[char]; found && val > 0 {
			copyDict[char]--
		} else {
			return false
		}
	}
	return true
}

func copyMap(originalMap map[int32]int) map[int32]int {
	copiedMap := make(map[int32]int)
	for key, value := range originalMap {
		copiedMap[key] = value
	}
	return copiedMap
}
