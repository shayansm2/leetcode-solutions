package main

func moveZeroesTwoPointer(nums []int) {
	slow := 0
	for fast := 0; fast < len(nums); fast++ {
		if nums[fast] == 0 {
			continue
		}
		nums[slow] = nums[fast]
		if fast > slow {
			nums[fast] = 0
		}
		slow++
	}
}
