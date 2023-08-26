package main

func rob(nums []int) int {
	var maxMoney [2]int
	for i, val := range nums {
		if i < 1 {
			maxMoney[i] = val
			continue
		}

		if i < 2 {
			maxMoney[i] = max(maxMoney[i-1], val)
			continue
		}

		maxMoney[i%2] = max(maxMoney[(i-1)%2], maxMoney[(i-2)%2]+val)
	}
	return maxMoney[(len(nums)-1)%2]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
