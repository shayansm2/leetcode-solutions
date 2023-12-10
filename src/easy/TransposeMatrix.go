package main

func transpose(matrix [][]int) [][]int {
	result := make([][]int, len(matrix[0]))
	for i := range result {
		result[i] = make([]int, len(matrix))
	}

	for i := range matrix {
		for j := range matrix[0] {
			result[j][i] = matrix[i][j]
		}
	}

	return result
}
