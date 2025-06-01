package main

import (
	"fmt"
	"math"
	"slices"
)

func minAbsDiff(grid [][]int, k int) [][]int {
	n := len(grid)
	m := len(grid[0])
	result := make([][]int, n-k+1)
	for i := range result {
		result[i] = make([]int, m-k+1)
	}
	if k == 1 {
		return result
	}
	for i := 0; i < n-k+1; i++ {
		// fmt.Println("i is", i)
		for j := 0; j < m-k+1; j++ {
			// fmt.Println("j is", j)
			elements := make([]int, 0)
			for ni := i; ni < i+k; ni++ {
				for nj := j; nj < j+k; nj++ {
					elements = append(elements, grid[ni][nj])
				}
			}
			// fmt.Println("elements are", elements)
			slices.Sort(elements)
			minDiff := float64(0)
			for e := 0; e < len(elements)-1; e++ {
				newDiff := math.Abs(float64(elements[e] - elements[e+1]))
				if newDiff == 0 {
					continue
				}
				if newDiff < minDiff || minDiff == 0 {
					minDiff = newDiff
				}
			}

			result[i][j] = int(minDiff)
		}
	}
	return result
}

func main() {
	fmt.Println([][]int{{1, 8}, {3, -2}}, 2, minAbsDiff([][]int{{1, 8}, {3, -2}}, 2))
	fmt.Println([][]int{{3, -1}}, 1, minAbsDiff([][]int{{3, -1}}, 1))
	fmt.Println([][]int{{1, -2, 3}, {2, 3, 5}}, 2, minAbsDiff([][]int{{1, -2, 3}, {2, 3, 5}}, 2))
}
