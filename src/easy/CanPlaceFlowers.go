package main

func canPlaceFlowers(flowerbed []int, n int) bool {
	filled := make([]bool, len(flowerbed))
	for i, flowered := range flowerbed {
		if flowered == 0 {
			continue
		}
		filled[i] = true
		if i > 0 {
			filled[i-1] = true
		}
		if i < len(flowerbed)-1 {
			filled[i+1] = true
		}
	}
	emptyCells := 0
	count := 0
	for _, v := range filled {
		if v {
			emptyCells += ((count + 1) / 2)
			count = 0
		} else {
			count++
		}
	}
	emptyCells += ((count + 1) / 2)
	return emptyCells >= n
}
