package main

func maxFrequencyElements(nums []int) int {
	freq := make(map[int]int)
	maxFreq := 0

	for _, num := range nums {
		if _, found := freq[num]; found {
			freq[num]++
		} else {
			freq[num] = 1
		}

		if maxFreq < freq[num] {
			maxFreq = freq[num]
		}
	}

	result := 0
	for _, count := range freq {
		if count == maxFreq {
			result += maxFreq
		}
	}

	return result
}
