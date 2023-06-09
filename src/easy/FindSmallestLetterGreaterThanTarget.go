package main

import "fmt"

func nextGreatestLetter(letters []byte, target byte) byte {
	index := letterBinarySearch(letters, target)

	for i := index - 1; i < len(letters); i++ {
		if i < 0 {
			continue
		}

		if letters[i] > target {
			return letters[i]
		}
	}

	return letters[0]
}

func letterBinarySearch(letters []byte, target byte) int {
	start, end := 0, len(letters)-1

	for start <= end {
		mid := (end-start)/2 + start

		if letters[mid] == target {
			return mid
		}

		if letters[mid] > target {
			end = mid - 1
		} else {
			start = mid + 1
		}
	}

	return start
}

func main() {
	testCases := []map[string]string{
		{
			"letters": "cfj",
			"target":  "a",
			"output":  "c",
		},
		{
			"letters": "cfj",
			"target":  "c",
			"output":  "f",
		},
		{
			"letters": "xxyy",
			"target":  "z",
			"output":  "x",
		},
		{
			"letters": "cfj",
			"target":  "d",
			"output":  "f",
		},
		{
			"letters": "cfj",
			"target":  "g",
			"output":  "j",
		},
		{
			"letters": "eegg",
			"target":  "g",
			"output":  "e",
		},
	}

	for _, testCase := range testCases {
		fmt.Println(string(nextGreatestLetter(
			[]byte(testCase["letters"]),
			[]byte(testCase["target"])[0],
		)), testCase["output"])
	}
}
