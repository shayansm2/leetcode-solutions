package main

import "strconv"

type WordDictionaryHashMap struct {
	indexLetters map[string][]string
}

func WordDictionaryHashMapConstructor() WordDictionaryHashMap {
	return WordDictionaryHashMap{indexLetters: make(map[string][]string)}
}

func (this *WordDictionaryHashMap) AddWord(word string) {
	for i, char := range word {
		key := strconv.Itoa(i) + "-" + string(char)
		if _, found := this.indexLetters[key]; !found {
			this.indexLetters[key] = make([]string, 0)
		}
		this.indexLetters[key] = append(this.indexLetters[key], word)
	}
}

func (this *WordDictionaryHashMap) Search(word string) bool {
	bestIndex := -1
	for i, char := range word {
		if string(char) == "." {
			continue
		}
		if bestIndex == -1 {
			bestIndex = i
		}
		key := strconv.Itoa(i) + "-" + string(char)
		if matches, found := this.indexLetters[key]; found && bestIndex > len(matches) {
			bestIndex = len(matches)
		}
	}

	if bestIndex == -1 {
		return this.checkAllWordsLength(word)
	}

	key := strconv.Itoa(bestIndex) + "-" + string(word[bestIndex])
	for _, potentialMatch := range this.indexLetters[key] {
		if this.match(word, potentialMatch) {
			return true
		}
	}
	return false
}

func (this *WordDictionaryHashMap) match(search, potential string) bool {
	if len(search) != len(potential) {
		return false
	}

	for i, char := range search {
		if string(char) == "." {
			continue
		}

		if string(char) != string(potential[i]) {
			return false
		}
	}

	return true
}

func (this *WordDictionaryHashMap) checkAllWordsLength(search string) bool {
	for _, words := range this.indexLetters {
		for _, word := range words {
			if len(search) == len(word) {
				return true
			}
		}
	}
	return false
}
