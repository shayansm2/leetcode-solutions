package main

func removeElement(nums []int, val int) int {
	index, replaceIndex := 0, len(nums)-1
	var counter int
	for index <= replaceIndex {
		if nums[index] == val {
			nums[index] = nums[replaceIndex]
			replaceIndex--
		} else {
			index++
			counter++
		}
	}
	return counter
}
