package main

import (
	"fmt"
	"sort"
)

type KthLargest struct {
	sortedArray []int
	k           int
}

func KthLargestConstructor(k int, nums []int) KthLargest {
	sort.Ints(nums)
	return KthLargest{sortedArray: nums, k: k}
}

func (this *KthLargest) Add(val int) int {
	this.add(val)
	return this.sortedArray[len(this.sortedArray)-this.k]
}

func (this *KthLargest) add(val int) {
	index := binarySearch(this.sortedArray, val)
	newArray := make([]int, len(this.sortedArray)+1)
	copy(newArray[:], this.sortedArray[:index])
	newArray[index] = val
	copy(newArray[index+1:], this.sortedArray[index:])
	this.sortedArray = newArray
}

func binarySearch(array []int, k int) int {
	start, end := 0, len(array)-1
	for start <= end {
		mid := start + ((end - start) / 2)
		if array[mid] == k {
			return mid
		}
		if array[mid] > k {
			end = mid - 1
		} else {
			start = mid + 1
		}
	}
	return start
}

func main() {
	obj := KthLargestConstructor(3, []int{4, 5, 8, 2})
	fmt.Println(obj.Add(3))  // 4
	fmt.Println(obj.Add(5))  // 5
	fmt.Println(obj.Add(10)) // 5
	fmt.Println(obj.Add(9))  // 8
	fmt.Println(obj.Add(4))  // 8
}
