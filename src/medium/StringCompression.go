package main

import "strconv"

func compress(chars []byte) int {
	wp := 0
	curChar := chars[0]
	count := 1
	for rp := 1; rp < len(chars); rp++ {
		if chars[rp] == curChar {
			count++
			continue
		}

		chars[wp] = curChar
		wp++
		if count > 1 {
			for _, char := range strconv.Itoa(count) {
				chars[wp] = byte(char)
				wp++
			}
		}
		curChar = chars[rp]
		count = 1
	}
	chars[wp] = curChar
	wp++
	if count > 1 {
		for _, char := range strconv.Itoa(count) {
			chars[wp] = byte(char)
			wp++
		}
	}
	return wp
}
