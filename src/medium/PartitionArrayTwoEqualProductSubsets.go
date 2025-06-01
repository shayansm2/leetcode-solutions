package main

import (
	"fmt"
)

func checkEqualPartitions(nums []int, target int64) bool {
	var product int64 = 1
	for _, num := range nums {
		if target%int64(num) != 0 {
			return false
		}
		if int64(num) > target {
			return false
		}
		product *= int64(num)
	}
	return product == target*target
}

func main() {
	fmt.Println(checkEqualPartitions([]int{3, 1, 6, 8, 4}, int64(24)))
	fmt.Println(checkEqualPartitions([]int{2, 5, 3, 7}, int64(24)))
	fmt.Println(checkEqualPartitions([]int{1, 1, 1}, int64(1)))
	fmt.Println(checkEqualPartitions([]int{1, 1, 1, 2}, int64(3)))
	fmt.Println(checkEqualPartitions([]int{11, 22, 5, 10}, int64(110)))

}
