package main

import (
	"fmt"
	"sort"
)

func minCost(nums []int, cost []int) int64 {
	numbers, accCosts, accNumberCosts := preProcessing(nums, cost)

	var minimumCost int64 = -1
	for i, number := range numbers {
		iterCost := calculateCost(accCosts, accNumberCosts, number, i)
		if minimumCost > 0 && minimumCost < iterCost {
			break
		}
		minimumCost = iterCost
	}

	return minimumCost
}

func calculateCost(costs []int, numberCosts []int, number int, i int) int64 {
	var leftSide, rightSide int64
	n := len(costs)

	if i > 0 {
		leftSide = int64(costs[i-1]*number) - int64(numberCosts[i-1])
	}

	if i < n-1 {
		rightSide = int64(numberCosts[n-1]-numberCosts[i]) - int64(number*(costs[n-1]-costs[i]))
	}

	return leftSide + rightSide
}

func preProcessing(nums []int, cost []int) ([]int, []int, []int) {
	indices := make([]int, len(nums))
	for i := range indices {
		indices[i] = i
	}

	sort.SliceStable(indices, func(i, j int) bool {
		return nums[indices[i]] < nums[indices[j]]
	})

	curCost, curNumberCost := 0, 0
	numbers, accCosts, accNumberCosts := make([]int, len(nums)), make([]int, len(nums)), make([]int, len(nums))

	for i, index := range indices {
		numbers[i] = nums[index]
		curCost += cost[index]
		accCosts[i] = curCost
		curNumberCost += numbers[i] * cost[index]
		accNumberCosts[i] = curNumberCost
	}

	return numbers, accCosts, accNumberCosts
}

func main() {
	fmt.Println(minCost([]int{1, 3, 5, 2}, []int{2, 3, 1, 14}))
}
