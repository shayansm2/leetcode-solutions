package main

import "fmt"

func destCity(paths [][]string) string {
	fromTo := make(map[string]string)
	for _, path := range paths {
		fromTo[path[0]] = path[1]
	}

	result := paths[0][0]
	for _, found := fromTo[result]; found; _, found = fromTo[result] {
		result = fromTo[result]
	}
	return result
}

func main() {
	fmt.Println(destCity([][]string{{"London", "New York"}, {"New York", "Lima"}, {"Lima", "Sao Paulo"}}))
}
