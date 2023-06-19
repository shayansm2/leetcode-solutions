package main

func largestAltitude(gain []int) int {
	curAltitude, maxAltitude := 0, 0
	for _, dif := range gain {
		curAltitude += dif
		if maxAltitude < curAltitude {
			maxAltitude = curAltitude
		}
	}
	return maxAltitude
}
