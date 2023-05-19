package main

import (
	"fmt"
	"sort"
)

func hIndex(citations []int) int {
	sort.Slice(citations, func(i, j int) bool {
		return citations[i] >= citations[j]
	})

	if citations[0] < 1 {
		return 0
	}

	for i, citation := range citations {
		if i+1 > citation {
			return i
		}
	}

	return len(citations)
}

func main() {
	fmt.Println(hIndex([]int{3, 0, 6, 1, 5}))
	fmt.Println(hIndex([]int{1, 3, 1}))
	fmt.Println(hIndex([]int{1}))
}
