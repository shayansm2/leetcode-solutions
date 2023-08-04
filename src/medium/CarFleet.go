package main

import (
	"fmt"
	"sort"
)

type Car struct {
	initPosition int
	speed        int
}

func carFleet(target int, position []int, speed []int) int {
	cars := make([]Car, len(position))
	for i := range position {
		cars[i] = Car{initPosition: position[i], speed: speed[i]}
	}

	sort.Slice(cars, func(i, j int) bool {
		return cars[i].initPosition < cars[j].initPosition
	}) // o(nlogn)

	result := len(cars)
	for back := 0; back < len(cars)-1; back++ { // o(n2)
		if willReachAnotherCar(back, cars, target) {
			result--
		}
	}
	return result
}

func willReachAnotherCar(back int, cars []Car, target int) bool {
	for front := back + 1; front < len(cars); front++ {
		if cars[back].initPosition == cars[front].initPosition {
			//fmt.Println(cars[back], cars[front])
			return true
		}

		if cars[back].speed <= cars[front].speed {
			continue
		}

		if collisionPoint(cars[front], cars[back]) <= float64(target) {
			//fmt.Println(cars[back], cars[front], collisionPoint(cars[front], cars[back]))
			return true
		}
	}
	return false
}

func collisionPoint(front, back Car) float64 {
	collisionTime := float64(front.initPosition-back.initPosition) / float64(back.speed-front.speed)
	return float64(back.initPosition) + collisionTime*float64(back.speed)
}

func main() {
	fmt.Println(carFleet(12, []int{10, 8, 0, 5, 3}, []int{2, 4, 1, 1, 3}), 3)
	fmt.Println(carFleet(10, []int{3}, []int{3}), 1)
	fmt.Println(carFleet(100, []int{0, 2, 4}, []int{4, 2, 1}), 1)
	fmt.Println(carFleet(10, []int{6, 8}, []int{3, 2}), 2)
	fmt.Println(carFleet(10, []int{0, 4, 2}, []int{2, 1, 3}), 1)
	fmt.Println(carFleet(13, []int{10, 2, 5, 7, 4, 6, 11}, []int{7, 5, 10, 5, 9, 4, 1}), 2)
}
