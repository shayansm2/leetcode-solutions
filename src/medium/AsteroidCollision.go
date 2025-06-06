package main

func asteroidCollision(asteroids []int) []int {
	stack := make([]int, 0)
	for len(asteroids) > 0 {
		newAsteroid := asteroids[0]
		if len(stack) == 0 || newAsteroid > 0 {
			stack = append(stack, newAsteroid)
			asteroids = asteroids[1:]
			continue
		}
		lastAstroid := stack[len(stack)-1]
		if lastAstroid < 0 {
			stack = append(stack, newAsteroid)
			asteroids = asteroids[1:]
			continue
		}
		if lastAstroid > -newAsteroid {
			asteroids = asteroids[1:]
			continue
		}
		stack = stack[:len(stack)-1]
		if lastAstroid+newAsteroid == 0 {
			asteroids = asteroids[1:]
		}
	}
	return stack
}
