package main

import "fmt"

func findSmallestSetOfVertices(n int, edges [][]int) []int {
	hasInFlow := make([]bool, n)

	for _, edge := range edges {
		hasInFlow[edge[1]] = true
	}

	var result []int

	for i, val := range hasInFlow {
		if val == false {
			result = append(result, i)
		}
	}

	return result
}

func main() {
	fmt.Println(findSmallestSetOfVertices(6, [][]int{{0, 1}, {0, 2}, {2, 5}, {3, 4}, {4, 2}}))
	fmt.Println(findSmallestSetOfVertices(5, [][]int{{0, 1}, {2, 1}, {3, 1}, {1, 4}, {2, 4}}))
}
