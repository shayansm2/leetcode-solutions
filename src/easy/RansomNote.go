package main

func canConstruct(ransomNote string, magazine string) bool {
	ransomNoteHashMap := make(map[int32]int)
	for _, letter := range ransomNote {
		ransomNoteHashMap[letter]++
	}

	magazineHashMap := make(map[int32]int)
	for _, letter := range magazine {
		magazineHashMap[letter]++
	}

	for letter, count := range ransomNoteHashMap {
		if count > magazineHashMap[letter] {
			return false
		}
	}
	return true
}
