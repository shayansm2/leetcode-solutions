package main

func countPermutations(complexity []int) int {
	result := 1
	for i := 1; i < len(complexity); i++ {
		// fmt.Println(i, complexity[i])
		if complexity[i] <= complexity[0] {
			return 0
		}
		result *= i
		result = result % 1000000007
		// fmt.Println("result", result)
	}
	return result
}
