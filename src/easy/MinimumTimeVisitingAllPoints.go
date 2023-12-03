package main

import "math"

func minTimeToVisitAllPoints(points [][]int) int {
	var result int
	for i := 0; i < len(points)-1; i++ {
		result += getDistance(points[i], points[i+1])
	}
	return result
}

func getDistance(a, b []int) int {
	x1, x2 := a[0], b[0]
	y1, y2 := a[1], b[1]
	x, y := math.Abs(float64(x1-x2)), math.Abs(float64(y1-y2))
	return int(math.Max(x, y))
}
