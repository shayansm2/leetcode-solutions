package main

func matrixSumQueries(n int, queries [][]int) int64 {
	isRowTaken, isColumnTaken := make([]bool, n), make([]bool, n)
	var matrixSum int64
	filledRows, filledColumns := n, n
	for i := len(queries) - 1; i >= 0; i-- {
		queryType, index, value := queries[i][0], queries[i][1], queries[i][2]
		if queryType == 0 && isRowTaken[index] == false {
			isRowTaken[index] = true
			matrixSum += int64(value * filledColumns)
			filledRows--
		} else if queryType == 1 && isColumnTaken[index] == false {
			isColumnTaken[index] = true
			matrixSum += int64(value * filledRows)
			filledColumns--
		}
	}
	return matrixSum
}
