package main

func checkStraightLine(coordinates [][]int) bool {
	if len(coordinates) == 2 {
		return true
	}

	firstNode, secondNode := coordinates[0], coordinates[1]

	if firstNode[0] == secondNode[0] {
		for i := 2; i < len(coordinates); i++ {
			if firstNode[0] != coordinates[i][0] {
				return false
			}
		}
		return true
	}

	var a, b float64
	a = float64(secondNode[1]-firstNode[1]) / float64(secondNode[0]-firstNode[0])
	b = float64(firstNode[1]) - a*float64(firstNode[0])

	for i := 2; i < len(coordinates); i++ {
		if a*float64(coordinates[i][0])+b != float64(coordinates[i][1]) {
			return false
		}
	}
	return true
}
