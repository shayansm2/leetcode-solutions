package main

import "strings"

func divides(t string, s string) bool { // o(n)
	if len(s)%len(t) != 0 {
		return false
	}
	l := len(t)
	for i := 0; i < len(s)/l; i++ {
		if s[i*l:(i+1)*l] != t {
			return false
		}
	}
	return true
}

func findMinComponent(str string) string { // o(n2)
	for i := 1; i <= len(str); i++ {
		if divides(str[:i], str) {
			return str[:i]
		}
	}
	return ""
}

func GCD(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func gcdOfStrings(str1 string, str2 string) string {
	minStr := str1
	maxStr := str2
	if len(str2) < len(str1) {
		minStr = str2
		maxStr = str1
	}

	component := findMinComponent(minStr) // o(n2)
	if len(component) == 0 {
		return component
	}
	if !divides(component, maxStr) {
		return ""
	}
	componentCount := GCD(len(maxStr)/len(component), len(minStr)/len(component))
	return strings.Repeat(component, componentCount)
}
