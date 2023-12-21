package main

import "sort"

func maxWidthOfVerticalArea(points [][]int) int {
	xs := make(map[int]bool)
	for _, point := range points {
		xs[point[0]] = true
	}

	var xPoints []int
	for x := range xs {
		xPoints = append(xPoints, x)
	}

	sort.Ints(xPoints)

	var result int
	for i := 1; i < len(xPoints); i++ {
		if distance := xPoints[i] - xPoints[i-1]; distance > result {
			result = distance
		}
	}
	return result
}
