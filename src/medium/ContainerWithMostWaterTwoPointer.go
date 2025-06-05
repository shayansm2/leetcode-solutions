package main

func maxArea(height []int) int {
	start := 0
	end := len(height) - 1
	result := 0
	for start < end {
		containerArea := min(height[start], height[end]) * (end - start)
		result = max(result, containerArea)
		if height[start] > height[end] {
			end--
		} else {
			start++
		}
	}
	return result
}
