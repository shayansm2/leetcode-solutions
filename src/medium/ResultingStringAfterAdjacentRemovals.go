package main

import (
	"fmt"
)

func resultingString(s string) string {
	var q []rune
	for _, char := range s {
		if len(q) == 0 {
			q = append(q, char)
			continue
		}
		if (char-q[len(q)-1] == 1) || (char-q[len(q)-1] == -1) {
			q = q[:len(q)-1]
			continue
		}
		if (char-q[len(q)-1] == 25) || (char-q[len(q)-1] == -25) {
			q = q[:len(q)-1]
			continue
		}
		q = append(q, char)
	}
	return string(q)
}

func main() {
	fmt.Println(resultingString("az"))
}
