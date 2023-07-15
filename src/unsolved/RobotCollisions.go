package main

import (
	"fmt"
	"math"
	"sort"
)

type Robot struct {
	order  int
	health int
}

func (this *Robot) decreaseHealth() {
	//fmt.Println(this.health)

	if this.health > 0 {
		this.health--
	} else {
		this.health++
	}

	//fmt.Println(this.health)
}

func survivedRobotsHealths(positions []int, healths []int, directions string) []int {
	indices := make([]int, len(positions))
	for i := range indices {
		indices[i] = i
	}

	// Sort the indices slice using a custom comparator function
	sort.Slice(indices, func(i, j int) bool {
		return positions[indices[i]] < positions[indices[j]]
	})

	var stack []Robot

	for _, order := range indices {
		fmt.Println(stack)

		direction := 1
		if string(directions[order]) == "L" {
			direction = -1
		}
		robot := Robot{order: order, health: healths[order] * direction}

		if len(stack) == 0 {
			stack = append(stack, robot)
		} else {
			head := stack[len(stack)-1]
			if head.health > 0 && robot.health < 0 {
				if head.health+robot.health == 0 {
					stack = stack[:len(stack)-1]
				} else if math.Abs(float64(head.health)) > math.Abs(float64(robot.health)) {
					stack[len(stack)-1].decreaseHealth()
				} else {
					stack = stack[:len(stack)-1]
					robot.decreaseHealth()
					stack = append(stack, robot)
				}
			} else {
				stack = append(stack, robot)
			}
		}
	}

	//fmt.Println(stack)

	// Sort the slice of structs by the order field
	sort.Slice(stack, func(i, j int) bool {
		return stack[i].order < stack[j].order
	})

	// Create a new slice of values sorted by order
	result := make([]int, len(stack))
	for i, v := range stack {
		result[i] = int(math.Abs(float64(v.health)))
	}

	return result
}

func main() {
	fmt.Println(survivedRobotsHealths([]int{11, 44, 16}, []int{1, 20, 17}, "RLR"))
}
