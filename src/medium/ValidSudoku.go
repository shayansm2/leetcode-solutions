package main

import "fmt"

const one = 49
const nine = 57
const dot = 46

func isValidSudoku(board [][]byte) bool {
	channel := make(chan bool)
	validateRows(board, channel)
	validateColumns(board, channel)
	validateSubBoxes(board, channel)

	for i := 0; i < 27; i++ {
		isValid := <-channel
		if isValid == false {
			return false
		}
	}
	return true
}

func validateRows(board [][]byte, channel chan bool) {
	for i := 0; i < 9; i++ {
		go validateRange(board, []int{i}, []int{0, 1, 2, 3, 4, 5, 6, 7, 8}, channel)
	}
}

func validateColumns(board [][]byte, channel chan bool) {
	for i := 0; i < 9; i++ {
		go validateRange(board, []int{0, 1, 2, 3, 4, 5, 6, 7, 8}, []int{i}, channel)
	}
}

func validateSubBoxes(board [][]byte, channel chan bool) {
	ranges := []map[string][]int{
		{"row": {0, 1, 2}, "col": {0, 1, 2}},
		{"row": {0, 1, 2}, "col": {3, 4, 5}},
		{"row": {0, 1, 2}, "col": {6, 7, 8}},
		{"row": {3, 4, 5}, "col": {0, 1, 2}},
		{"row": {3, 4, 5}, "col": {3, 4, 5}},
		{"row": {3, 4, 5}, "col": {6, 7, 8}},
		{"row": {6, 7, 8}, "col": {0, 1, 2}},
		{"row": {6, 7, 8}, "col": {3, 4, 5}},
		{"row": {6, 7, 8}, "col": {6, 7, 8}},
	}

	for _, subBox := range ranges {
		go validateRange(board, subBox["row"], subBox["col"], channel)
	}
}

func validateRange(board [][]byte, rowRange []int, columnRange []int, channel chan bool) {
	digitMap := make(map[byte]int, 9)
	for _, row := range rowRange {
		for _, column := range columnRange {
			digit := board[row][column]
			if digit == dot {
				continue
			}

			if digit < one {
				channel <- false
			}

			if digit > nine {
				channel <- false
			}

			if digitMap[digit] > 0 {
				channel <- false
			}

			digitMap[digit]++
		}
	}
	channel <- true
}

func main() {
	//board := [][]string{
	//	{"5", "3", ".", ".", "7", ".", ".", ".", "."},
	//	{"6", ".", ".", "1", "9", "5", ".", ".", "."},
	//	{".", "9", "8", ".", ".", ".", ".", "6", "."},
	//	{"8", ".", ".", ".", "6", ".", ".", ".", "3"},
	//	{"4", ".", ".", "8", ".", "3", ".", ".", "1"},
	//	{"7", ".", ".", ".", "2", ".", ".", ".", "6"},
	//	{".", "6", ".", ".", ".", ".", "2", "8", "."},
	//	{".", ".", ".", "4", "1", "9", ".", ".", "5"},
	//	{".", ".", ".", ".", "8", ".", ".", "7", "9"},
	//}

	board := [][]string{
		{"8", "3", ".", ".", "7", ".", ".", ".", "."},
		{"6", ".", ".", "1", "9", "5", ".", ".", "."},
		{".", "9", "8", ".", ".", ".", ".", "6", "."},
		{"8", ".", ".", ".", "6", ".", ".", ".", "3"},
		{"4", ".", ".", "8", ".", "3", ".", ".", "1"},
		{"7", ".", ".", ".", "2", ".", ".", ".", "6"},
		{".", "6", ".", ".", ".", ".", "2", "8", "."},
		{".", ".", ".", "4", "1", "9", ".", ".", "5"},
		{".", ".", ".", ".", "8", ".", ".", "7", "9"},
	}

	input := make([][]byte, len(board))
	for i, row := range board {
		inputRow := make([]byte, len(board))
		for j, char := range row {
			inputRow[j] = []byte(char)[0]
		}
		input[i] = inputRow
	}

	fmt.Println(isValidSudoku(input))
}
