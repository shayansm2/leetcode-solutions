package main

import "fmt"

func numberOfWays(corridor string) int {
	seatCount := 0
	plantCount := 0
	result := 1
	modulo := 1000000007
	for _, object := range corridor {
		if object == 'S' {
			seatCount++
			if seatCount%2 == 1 && seatCount > 2 {
				result *= (plantCount + 1) % modulo
				result %= modulo
			}
			plantCount = 0
		} else if object == 'P' {
			plantCount++
		}
	}
	if seatCount%2 == 1 || seatCount < 2 {
		return 0
	}
	return result
}

func main() {
	fmt.Println(numberOfWays("SSPPSPS"), 3)
	fmt.Println(numberOfWays("SPPPSPPSPS"), 3)
	fmt.Println(numberOfWays("PPSPSP"), 1)
	fmt.Println(numberOfWays("S"), 0)
	fmt.Println(numberOfWays("P"), 0)
	fmt.Println(numberOfWays("SPPPSPPSPSPPS"), 0)
}
