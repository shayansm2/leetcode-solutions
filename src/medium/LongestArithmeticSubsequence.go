package main

func longestArithSeqLength(nums []int) int {
	arithmeticSequences := make(map[[2]int]int)
	longestArithmeticSeqLength := 0
	for i := 1; i < len(nums); i++ {
		number1 := nums[i]
		for j, number2 := range nums[:i] {
			if length, exists := arithmeticSequences[[2]int{j, number1 - number2}]; exists {
				arithmeticSequences[[2]int{i, number1 - number2}] = length + 1
			} else {
				arithmeticSequences[[2]int{i, number1 - number2}] = 2
			}

			if arithmeticSequences[[2]int{i, number1 - number2}] > longestArithmeticSeqLength {
				longestArithmeticSeqLength = arithmeticSequences[[2]int{i, number1 - number2}]
			}
		}
	}
	//fmt.Println(arithmeticSequences)
	return longestArithmeticSeqLength
}

func main() {
	println(longestArithSeqLength([]int{12, 28, 13, 6, 34, 36, 53, 24, 29, 2, 23, 0, 22, 25, 53, 34, 23, 50, 35, 43, 53, 11, 48, 56, 44, 53, 31, 6, 31, 57, 46, 6, 17, 42, 48, 28, 5, 24, 0, 14, 43, 12, 21, 6, 30, 37, 16, 56, 19, 45, 51, 10, 22, 38, 39, 23, 8, 29, 60, 18}))
}
