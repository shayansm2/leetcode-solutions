package main

func partitionString(s string) []string {
	hashmap := make(map[string]bool)
	result := make([]string, 0)
	start := 0
	for end := 0; end < len(s); end++ {
		segment := string(s[start : end+1])
		if _, found := hashmap[segment]; !found {
			hashmap[segment] = true
			result = append(result, segment)
			start = end + 1
		}
	}
	return result
}
