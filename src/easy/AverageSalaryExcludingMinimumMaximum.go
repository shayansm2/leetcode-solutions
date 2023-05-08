package main

import "fmt"

func main() {
	fmt.Println(average([]int{4000, 3000, 1000, 2000}))
	fmt.Println(average([]int{1000, 2000, 3000}))
}

func average(salary []int) float64 {
	var sum, counter int
	min, max := 1000001, 999

	for _, val := range salary {
		sum += val
		counter++

		if min > val {
			min = val
		}

		if max < val {
			max = val
		}
	}

	sum -= min + max
	counter -= 2

	return float64(sum) / float64(counter)
}
