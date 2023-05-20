package main

import "fmt"

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	graph := createGraph(equations, values)
	var result []float64

	for _, query := range queries {
		result = append(result, dfs(graph, query))
	}

	return result
}

func createGraph(equations [][]string, values []float64) map[string]map[string]float64 {
	graph := make(map[string]map[string]float64)
	for i, equation := range equations {
		_, keyExists := graph[equation[0]]
		if keyExists == false {
			graph[equation[0]] = make(map[string]float64)
		}
		graph[equation[0]][equation[1]] = values[i]
		_, keyExists = graph[equation[1]]
		if keyExists == false {
			graph[equation[1]] = make(map[string]float64)
		}
		graph[equation[1]][equation[0]] = 1 / values[i]
	}
	return graph
}

func dfs(graph map[string]map[string]float64, query []string) float64 {
	from, to := query[0], query[1]

	_, exists := graph[from]
	if exists == false {
		return -1
	}

	_, exists = graph[to]
	if exists == false {
		return -1
	}

	stack := []string{from}
	divisions := make(map[string]float64)
	divisions[from] = 1
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		neighbours := graph[node]

		for neighbour, distance := range neighbours {
			if neighbour == to {
				return divisions[node] * distance
			}

			_, visited := divisions[neighbour]
			if visited == false {
				divisions[neighbour] = divisions[node] * distance
				stack = append(stack, neighbour)
			}
		}
	}

	return -1
}

func main() {
	fmt.Println(calcEquation(
		[][]string{{"a", "b"}, {"b", "c"}},
		[]float64{2, 3},
		[][]string{{"a", "c"}, {"b", "a"}, {"a", "e"}, {"a", "a"}, {"x", "x"}},
	))
	fmt.Println(calcEquation(
		[][]string{{"a", "b"}, {"b", "c"}, {"bc", "cd"}},
		[]float64{1.5, 2.5, 5.0},
		[][]string{{"a", "c"}, {"c", "b"}, {"bc", "cd"}, {"cd", "bc"}},
	))
	fmt.Println(calcEquation(
		[][]string{{"a", "b"}},
		[]float64{0.5},
		[][]string{{"a", "b"}, {"b", "a"}, {"a", "c"}, {"x", "y"}},
	))
}
