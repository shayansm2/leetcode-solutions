package main

func maxProfit(prices []int) int {
	minSoFar, maximumProfit := prices[0], 0

	for _, price := range prices {
		if price < minSoFar {
			minSoFar = price
		}

		if maximumProfit < price-minSoFar {
			maximumProfit = price - minSoFar
		}
	}

	return maximumProfit
}
