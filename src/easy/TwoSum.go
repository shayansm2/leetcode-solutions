package main

func twoSum(nums []int, target int) []int {
	numberIndices := make(map[int]int)
	for i, num := range nums {
		index, found := numberIndices[target-num]
		if found {
			return []int{i, index}
		}
		numberIndices[num] = i
	}
	return []int{}
}
