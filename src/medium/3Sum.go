package main

import (
	"fmt"
	"sort"
	"strconv"
)

func threeSum(nums []int) [][]int {
	sort.Ints(nums)

	counter := make(map[int]int)
	for _, num := range nums {
		if _, found := counter[num]; found {
			counter[num]++
		} else {
			counter[num] = 1
		}
	}

	uniqueTriples := make(map[string][]int)
	for i := 0; i < len(nums)-2; i++ {
		if nums[i] > 0 {
			break
		}
		for j := i + 1; j < len(nums)-1; j++ {
			if nums[i]+nums[j] > 0 {
				break
			}

			find := -nums[i] - nums[j]
			if find < nums[j] {
				break
			}
			count, found := counter[find]

			if find > nums[j] && found && count > 0 {
				uniqueTriples[getKey(nums[i], nums[j], find)] = []int{nums[i], nums[j], find}
				continue
			}

			if find > nums[i] && found && count > 1 {
				uniqueTriples[getKey(nums[i], nums[j], find)] = []int{nums[i], nums[j], find}
				continue
			}

			if found && count > 2 {
				uniqueTriples[getKey(nums[i], nums[j], find)] = []int{nums[i], nums[j], find}
			}
		}
	}

	var result [][]int
	for _, val := range uniqueTriples {
		result = append(result, val)
	}
	return result
}

func getKey(a, b, c int) string {
	return strconv.Itoa(a) + "-" + strconv.Itoa(b) + "-" + strconv.Itoa(c)
}

func main() {
	fmt.Println(threeSum([]int{-1, 0, 1, 2, -1, -4}))
	fmt.Println(threeSum([]int{0, 1, 1}))
	fmt.Println(threeSum([]int{0, 0, 0}))
	fmt.Println(threeSum([]int{-2, 0, 0, 2, 2}))
}
