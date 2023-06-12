package main

import "strconv"

func summaryRanges(nums []int) []string {
	if len(nums) == 0 {
		return []string{}
	}

	if len(nums) == 1 {
		return []string{strconv.Itoa(nums[0])}
	}

	var ranges []string
	rangeStart, rangeEnd := nums[0], nums[0]

	for i := 1; i < len(nums); i++ {
		cur := nums[i]
		if cur == rangeEnd+1 {
			rangeEnd = cur
			continue
		}

		if rangeStart == rangeEnd {
			ranges = append(ranges, strconv.Itoa(rangeStart))
		} else {
			ranges = append(ranges, strconv.Itoa(rangeStart)+"->"+strconv.Itoa(rangeEnd))
		}

		rangeStart, rangeEnd = cur, cur
	}

	if rangeStart == rangeEnd {
		ranges = append(ranges, strconv.Itoa(rangeStart))
	} else {
		ranges = append(ranges, strconv.Itoa(rangeStart)+"->"+strconv.Itoa(rangeEnd))
	}

	return ranges
}
