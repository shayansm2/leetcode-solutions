package main

import "fmt"

func main() {
	fmt.Println(generateMatrix(3))
	fmt.Println(generateMatrix(1))
}

func generateMatrix(n int) [][]int {
	matrix := make([][]int, n)
	for i := range matrix {
		matrix[i] = make([]int, n)
	}

	i, j := 0, 0
	dir := "right"
	for counter := 1; counter < n*n; counter++ {
		matrix[i][j] = counter
		dir = getNextDirection(i, j, matrix, dir)
		i, j = getNextCoordination(i, j, dir)
	}
	matrix[i][j] = n * n

	return matrix
}

func getNextDirection(i int, j int, matrix [][]int, dir string) string {
	nextDirs := map[string]string{
		"right": "down",
		"down":  "left",
		"left":  "up",
		"up":    "right",
	}

	newI, newJ := getNextCoordination(i, j, dir)
	if newI < 0 || newI >= len(matrix) {
		return nextDirs[dir]
	}

	if newJ < 0 || newJ >= len(matrix) {
		return nextDirs[dir]
	}

	if matrix[newI][newJ] > 0 {
		return nextDirs[dir]
	}

	return dir
}

func getNextCoordination(i int, j int, direction string) (int, int) {
	if direction == "right" {
		return i, j + 1
	}

	if direction == "left" {
		return i, j - 1
	}

	if direction == "up" {
		return i - 1, j
	}

	if direction == "down" {
		return i + 1, j
	}

	return 0, 0
}
