package main

import (
	"fmt"
)

func ConcurrentMaximumDetonation(bombs [][]int) int {
	graph := createDirectedGraph(bombs)
	return ConcurrentDFSAndGetMax(graph)
}

func ConcurrentDFSAndGetMax(graph []BombNode) int {
	maxVisits := 1
	channel := make(chan int)
	for startNode := range graph {
		go dfsAndGetVisitsCount(graph, startNode, channel)
	}
	for i := range graph {
		_ = i
		visitsCount := <-channel
		if visitsCount > maxVisits {
			maxVisits = visitsCount
		}
	}
	return maxVisits
}

func dfsAndGetVisitsCount(graph []BombNode, startNode int, channel chan int) {
	visited := make(map[int]bool)
	queue := []int{startNode}
	visited[startNode] = true
	for len(queue) > 0 {
		curNode := queue[0]
		queue = queue[1:]
		for _, neighbor := range graph[curNode].neighbors {
			if visited[neighbor] {
				continue
			}
			queue = append(queue, neighbor)
			visited[neighbor] = true
		}
	}
	channel <- len(visited)
}

func main() {
	fmt.Println(ConcurrentMaximumDetonation([][]int{{2, 1, 3}, {6, 1, 4}}))                                  // 2
	fmt.Println(ConcurrentMaximumDetonation([][]int{{1, 1, 5}, {10, 10, 5}}))                                // 1
	fmt.Println(ConcurrentMaximumDetonation([][]int{{1, 2, 3}, {2, 3, 1}, {3, 4, 2}, {4, 5, 3}, {5, 6, 4}})) // 5
}
