package main

func uniqueOccurrences(arr []int) bool {
	occurance := make(map[int]int)
	for _, i := range arr {
		occurance[i] = occurance[i] + 1
	}
	check := make(map[int]bool)
	for _, i := range occurance {
		if _, found := check[i]; found {
			return false
		}
		check[i] = true
	}
	return true
}
