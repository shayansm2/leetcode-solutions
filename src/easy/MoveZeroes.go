package main

func moveZeroes(nums []int) {
	lastIndex := len(nums) - 1
	curIndex := 0
	for curIndex <= lastIndex {
		if nums[curIndex] != 0 {
			curIndex++
			continue
		}
		for j := curIndex; j < lastIndex; j++ {
			nums[j] = nums[j+1]
		}
		nums[lastIndex] = 0
		lastIndex--
	}
}
