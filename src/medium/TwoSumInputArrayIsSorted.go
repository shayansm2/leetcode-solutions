package main

func twoSum(numbers []int, target int) []int {
	start, end := 0, len(numbers)-1

	for start < end {
		res := numbers[start] + numbers[end]

		if res == target {
			return []int{start + 1, end + 1}
		}

		if res > target {
			end--
		} else {
			start++
		}
	}

	return []int{}
}
