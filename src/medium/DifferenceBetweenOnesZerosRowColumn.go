package main

func onesMinusZeros(grid [][]int) [][]int {
	onesRow := make([]int, len(grid))
	zerosRow := make([]int, len(grid))
	onesCol := make([]int, len(grid[0]))
	zerosCol := make([]int, len(grid[0]))

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				onesRow[i]++
				onesCol[j]++
			} else {
				zerosRow[i]++
				zerosCol[j]++
			}
		}
	}

	result := make([][]int, len(grid))
	for i := range result {
		result[i] = make([]int, len(grid[0]))
	}
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			result[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
		}
	}
	return result
}
