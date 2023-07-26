package main

import "fmt"

func longestConsecutive(nums []int) int {
	starts, ends := make(map[int]int), make(map[int]int)
	for _, num := range nums {
		var addRecord = true

		if _, found := starts[num]; found {
			continue
		}

		if _, found := ends[num]; found {
			continue
		}

		if _, found := starts[num+1]; found {
			shiftStart(&starts, &ends, num+1)
			if _, foundForMerge := ends[num]; foundForMerge {
				mergeRanges(&starts, &ends, num)
			}
			addRecord = false
		}

		if _, found := ends[num-1]; found {
			shiftEnd(&starts, &ends, num-1)
			if _, foundForMerge := starts[num]; foundForMerge {
				mergeRanges(&starts, &ends, num)
			}
			addRecord = false
		}

		if addRecord {
			addRange(&starts, &ends, num, num)
		}
	}

	result := 0
	for start, end := range starts {
		if result < end-start+1 {
			result = end - start + 1
		}
	}
	return result
}

func mergeRanges(starts, ends *map[int]int, border int) {
	addRange(starts, ends, (*ends)[border], (*starts)[border])
	delete(*starts, border)
	delete(*ends, border)
}

func shiftEnd(starts, ends *map[int]int, end int) {
	addRange(starts, ends, (*ends)[end], end+1)
	delete(*ends, end)
}

func shiftStart(starts, ends *map[int]int, start int) {
	addRange(starts, ends, start-1, (*starts)[start])
	delete(*starts, start)
}

func addRange(starts, ends *map[int]int, start, end int) {
	(*starts)[start] = end
	(*ends)[end] = start
}

func main() {
	fmt.Println(longestConsecutive([]int{100, 4, 200, 1, 3, 2}))
	fmt.Println(longestConsecutive([]int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}))
	fmt.Println(longestConsecutive([]int{-7, -1, 3, -9, -4, 7, -3, 2, 4, 9, 4, -9, 8, -7, 5, -1, -7}))
	fmt.Println(longestConsecutive([]int{7, -9, 3, -6, 3, 5, 3, 6, -2, -5, 8, 6, -4, -6, -4, -4, 5, -9, 2, 7, 0, 0}))
}
