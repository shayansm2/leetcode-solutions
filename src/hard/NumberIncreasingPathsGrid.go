package main

import "fmt"

const modulo = 1000000007

func countPaths(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	CountPaths := 0

	cells := make([][][2]int, 100001)

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if cells[grid[i][j]] == nil {
				cells[grid[i][j]] = [][2]int{}
			}

			cells[grid[i][j]] = append(cells[grid[i][j]], [2]int{i, j})
		}
	}

	counters := make([][]int, m)
	for i := range counters {
		counters[i] = make([]int, n)
	}

	for _, cellArray := range cells {
		if cellArray == nil {
			continue
		}

		for _, cell := range cellArray {
			x, y := cell[0], cell[1]
			counters[x][y] = 1

			if x > 0 && grid[x][y] > grid[x-1][y] {
				counters[x][y] += counters[x-1][y] % modulo
			}

			if y > 0 && grid[x][y] > grid[x][y-1] {
				counters[x][y] += counters[x][y-1] % modulo
			}

			if x < m-1 && grid[x][y] > grid[x+1][y] {
				counters[x][y] += counters[x+1][y] % modulo
			}

			if y < n-1 && grid[x][y] > grid[x][y+1] {
				counters[x][y] += counters[x][y+1] % modulo
			}

			counters[x][y] %= modulo
			CountPaths += counters[x][y]
			CountPaths %= modulo
		}
	}

	return CountPaths
}

func main() {
	fmt.Println(countPaths([][]int{{1, 1}, {3, 4}}))
	fmt.Println(countPaths([][]int{{1}, {2}}))
	fmt.Println(countPaths([][]int{{1, 2, 3}, {6, 5, 4}, {1, 5, 9}}))
	fmt.Println(countPaths([][]int{{1, 2, 3, 1}, {6, 5, 4, 2}, {1, 5, 9, 0}}))
}
