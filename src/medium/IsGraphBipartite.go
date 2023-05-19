package main

import "fmt"

func isBipartite(graph [][]int) bool {
	flags := make([]int, len(graph))

	for i := range graph {
		if flags[i] != 0 {
			continue
		}

		queue := []int{i}
		flags[i] = 1

		for len(queue) > 0 {
			node := queue[len(queue)-1]
			queue = queue[:len(queue)-1]
			nodeFlag := flags[node]

			for _, neighbour := range graph[node] {
				if flags[neighbour] == nodeFlag {
					return false
				}

				if flags[neighbour] == 0 {
					queue = append(queue, neighbour)
					flags[neighbour] = -nodeFlag
				}
			}
		}
	}
	return true
}

func main() {
	fmt.Println(isBipartite([][]int{{1, 2, 3}, {0, 2}, {0, 1, 3}, {0, 2}}))
	fmt.Println(isBipartite([][]int{{1, 3}, {0, 2}, {1, 3}, {0, 2}}))
	fmt.Println(isBipartite([][]int{{}, {2, 4, 6}, {1, 4, 8, 9}, {7, 8}, {1, 2, 8, 9}, {6, 9}, {1, 5, 7, 8, 9}, {3, 6, 9}, {2, 3, 4, 6, 9}, {2, 4, 5, 6, 7, 8}}))
}
