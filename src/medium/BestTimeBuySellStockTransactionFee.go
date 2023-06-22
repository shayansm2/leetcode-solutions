package main

func maxProfit(prices []int, fee int) int {
	maximumProfit := 0
	minSoFar, maxSoFar := prices[0], prices[0]

	for _, price := range prices[1:] {
		//fmt.Println(price, minSoFar, maxSoFar, maximumProfit)
		if price > maxSoFar {
			maxSoFar = price
		} else if price < maxSoFar-fee || price < minSoFar {
			if maxSoFar-minSoFar > fee {
				maximumProfit += maxSoFar - minSoFar - fee
			}
			minSoFar, maxSoFar = price, price
		}
	}

	if maxSoFar-minSoFar > fee {
		maximumProfit += maxSoFar - minSoFar - fee
	}

	return maximumProfit
}
