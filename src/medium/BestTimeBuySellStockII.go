package main

import "fmt"

func maxProfitBuySellStock(prices []int) int {
	localMin := prices[0]
	var profit int
	for i := 1; i < len(prices); i++ {
		if prices[i] < prices[i-1] {
			profit += prices[i-1] - localMin
			localMin = prices[i]
		}
	}
	profit += prices[len(prices)-1] - localMin
	return profit
}

func main() {
	fmt.Println(maxProfitBuySellStock([]int{7, 1, 5, 3, 6, 4}))
	fmt.Println(maxProfitBuySellStock([]int{1, 2, 3, 4, 5}))
	fmt.Println(maxProfitBuySellStock([]int{7, 6, 4, 3, 1}))
}
