package main

import "strconv"

func evalRPN(tokens []string) int {
	var stack []int
	var newElement int
	for _, token := range tokens {
		if token == "+" || token == "-" || token == "*" || token == "/" {
			second := stack[len(stack)-1]
			first := stack[len(stack)-2]
			stack = stack[:len(stack)-2]
			if token == "+" {
				newElement = first + second
			} else if token == "-" {
				newElement = first - second
			} else if token == "*" {
				newElement = first * second
			} else if token == "/" {
				newElement = first / second
			}
		} else {
			newElement, _ = strconv.Atoi(token)
		}
		stack = append(stack, newElement)
	}
	return stack[0]
}
