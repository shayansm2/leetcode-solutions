package main

import "strconv"

type coordinate struct {
	x, y int
}

func (this *coordinate) move(direction string) {
	switch direction {
	case "N":
		this.y++
	case "S":
		this.y--
	case "E":
		this.x++
	case "W":
		this.x--
	}
}

func (this *coordinate) repr() string {
	return strconv.Itoa(this.x) + "-" + strconv.Itoa(this.y)
}

func isPathCrossing(path string) bool {
	visits := make(map[string]bool)
	current := &coordinate{0, 0}

	for _, direction := range path {
		visits[current.repr()] = true
		current.move(string(direction))
		if _, found := visits[current.repr()]; found {
			return true
		}
	}

	return false
}
