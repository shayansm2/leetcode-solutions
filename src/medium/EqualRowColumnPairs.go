package main

func equalPairs(grid [][]int) int {
	n, counter := len(grid), 0
	ch := make(chan bool, n*n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			go isRowAndColumnEqual(grid, i, j, ch)
		}
	}

	for i := 0; i < n*n; i++ {
		res := <-ch
		if res {
			counter++
		}
	}

	return counter
}

func isRowAndColumnEqual(grid [][]int, rowIndex int, columnIndex int, channel chan bool) {
	for k := 0; k < len(grid); k++ {
		if grid[rowIndex][k] != grid[k][columnIndex] {
			channel <- false
			return
		}
	}
	channel <- true
}
