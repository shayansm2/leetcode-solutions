package main

import "fmt"

func shortestPathBinaryMatrix(grid [][]int) int {
	if grid[0][0] == 1 {
		return -1
	}

	length := len(grid)
	if grid[length-1][length-1] == 1 {
		return -1
	}

	queue := [][2]int{{0, 0}}
	distances := make(map[[2]int]int)
	distances[[2]int{0, 0}] = 1

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur == [2]int{length - 1, length - 1} {
			return distances[cur]
		}

		for _, neighbour := range getNeighbours(grid, cur) {
			if distances[neighbour] <= distances[cur]+1 && distances[neighbour] > 0 {
				continue
			}
			queue = append(queue, neighbour)
			distances[neighbour] = distances[cur] + 1
		}
	}

	return -1
}

func getNeighbours(grid [][]int, cur [2]int) [][2]int {
	n := len(grid)
	row := cur[0]
	column := cur[1]
	var result [][2]int

	if row < n-1 && column < n-1 && grid[row+1][column+1] == 0 {
		result = append(result, [2]int{row + 1, column + 1})
	}

	if row < n-1 && grid[row+1][column] == 0 {
		result = append(result, [2]int{row + 1, column})
	}

	if column < n-1 && grid[row][column+1] == 0 {
		result = append(result, [2]int{row, column + 1})
	}

	if row > 0 && column < n-1 && grid[row-1][column+1] == 0 {
		result = append(result, [2]int{row - 1, column + 1})
	}

	if row < n-1 && column > 0 && grid[row+1][column-1] == 0 {
		result = append(result, [2]int{row + 1, column - 1})
	}

	if row > 0 && grid[row-1][column] == 0 {
		result = append(result, [2]int{row - 1, column})
	}

	if column > 0 && grid[row][column-1] == 0 {
		result = append(result, [2]int{row, column - 1})
	}

	if row > 0 && column > 0 && grid[row-1][column-1] == 0 {
		result = append(result, [2]int{row - 1, column - 1})
	}

	return result
}

func main() {
	fmt.Println(shortestPathBinaryMatrix([][]int{{0, 1}, {1, 0}}))
	fmt.Println(shortestPathBinaryMatrix([][]int{{0, 0, 0}, {1, 1, 0}, {1, 1, 0}}))
	fmt.Println(shortestPathBinaryMatrix([][]int{{1, 0, 0}, {1, 1, 0}, {1, 1, 0}}))
}
