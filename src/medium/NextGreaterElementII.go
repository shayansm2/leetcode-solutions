package main

import "fmt"

func nextGreaterElements(nums []int) []int {
	result := make([]int, len(nums))
	for i := range nums {
		result[i] = -1
	}

	type elementData struct {
		index int
		value int
	}
	var descStack []elementData // elements which there is no greater element number for them yet

	for i, val := range nums {
		for len(descStack) > 0 && descStack[len(descStack)-1].value < val {
			result[descStack[len(descStack)-1].index] = val
			descStack = descStack[:len(descStack)-1]
		}
		descStack = append(descStack, elementData{i, val})
	}

	for _, val := range nums {
		if len(descStack) == 0 {
			break
		}
		for result[descStack[len(descStack)-1].index] == -1 && descStack[len(descStack)-1].value < val {
			result[descStack[len(descStack)-1].index] = val
			descStack = descStack[:len(descStack)-1]
		}
	}

	return result
}

func main() {
	fmt.Println(nextGreaterElements([]int{1, 2, 1}), []int{2, -1, 2})
}
