package main

import "fmt"

func findKthLargest(nums []int, k int) int {
	fmt.Println(nums)
	return quickSort(nums, 0, len(nums)-1, k)
}

func quickSort(nums []int, start int, end int, k int) int {
	if start == end {
		return nums[start]
	}

	pivotIndex := start + ((end - start) / 2)
	pivotIndex = partition(nums, start, end, pivotIndex)

	if pivotIndex == k-1 {
		return nums[k-1]
	} else if pivotIndex < k-1 {
		return quickSort(nums, pivotIndex+1, end, k)
	} else {
		return quickSort(nums, start, pivotIndex-1, k)
	}
}

func partition(nums []int, start int, end int, pivotIndex int) int {
	pivotValue := nums[pivotIndex]
	nums[pivotIndex], nums[end] = nums[end], nums[pivotIndex]
	index := start

	for i := start; i < end; i++ {
		if nums[i] <= pivotValue {
			continue
		}
		nums[i], nums[index] = nums[index], nums[i]
		index++
	}

	nums[index], nums[end] = nums[end], nums[index]
	fmt.Println(index, nums)
	return index
}

func main() {
	fmt.Println(findKthLargest([]int{3, 2, 1, 5, 6, 4}, 2))
}
