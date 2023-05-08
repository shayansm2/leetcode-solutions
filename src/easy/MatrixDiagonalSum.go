package main

import "fmt"

func main() {
	fmt.Println(diagonalSum([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}))
	fmt.Println(diagonalSum([][]int{{1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}}))
	fmt.Println(diagonalSum([][]int{{5}}))
}

func diagonalSum(mat [][]int) int {
	var sum int
	length := len(mat)

	for i := 0; i < length; i++ {
		sum += mat[i][i]
		sum += mat[i][length-i-1]
	}

	if length%2 == 1 {
		sum -= mat[length/2][length/2]
	}

	return sum
}
