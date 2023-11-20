package main

import "strings"

func garbageCollection(garbage []string, travel []int) int {
	var lastMetalIndex, lastPaperIndex, lastGlassIndex, result int
	for i := len(garbage) - 1; i >= 0; i-- {
		if lastPaperIndex > 0 && lastGlassIndex > 0 && lastMetalIndex > 0 {
			break
		}

		if lastMetalIndex == 0 && strings.Contains(garbage[i], "M") {
			lastMetalIndex = i
		}

		if lastPaperIndex == 0 && strings.Contains(garbage[i], "P") {
			lastPaperIndex = i
		}

		if lastGlassIndex == 0 && strings.Contains(garbage[i], "G") {
			lastGlassIndex = i
		}
	}

	for _, garbageItem := range garbage {
		result += len(garbageItem)
	}

	distance := make([]int, len(garbage))
	distance[0] = 0
	i := 1

	for _, travelTime := range travel {
		distance[i] = distance[i-1] + travelTime
		i++
	}

	result += distance[lastGlassIndex] + distance[lastMetalIndex] + distance[lastPaperIndex]

	return result
}
