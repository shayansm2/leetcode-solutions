package main

func maxProduct(nums []int) int {
	firstMax, secondMax := 0, 0
	for _, num := range nums {
		if num >= firstMax {
			secondMax = firstMax
			firstMax = num
		} else if num > secondMax {
			secondMax = num
		}
	}
	return (firstMax - 1) * (secondMax - 1)
}
