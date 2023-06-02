package main

import (
	"fmt"
	"math"
)

type BombNode struct {
	id        int
	neighbors []int
}

func (this *BombNode) addNeighbor(id int) {
	this.neighbors = append(this.neighbors, id)
}

func maximumDetonation(bombs [][]int) int {
	graph := createDirectedGraph(bombs)
	return dfsAndGetMax(graph)
}

func createDirectedGraph(bombs [][]int) []BombNode {
	graph := make([]BombNode, len(bombs))
	for i, bomb := range bombs {
		A, B, R := bomb[0], bomb[1], bomb[2]
		node := BombNode{id: i}
		for j := 0; j < len(bombs); j++ {
			if j == i {
				continue
			}
			a, b := bombs[j][0], bombs[j][1]
			if getDistance(A, a, B, b) <= float64(R) {
				node.addNeighbor(j)
			}
		}
		graph[i] = node
	}
	return graph
}

func dfsAndGetMax(graph []BombNode) int {
	maxVisits := 1
	for startNode := range graph {
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
		if len(visited) > maxVisits {
			maxVisits = len(visited)
		}
	}
	return maxVisits
}

func getDistance(x1, x2, y1, y2 int) float64 {
	return math.Sqrt(math.Pow(float64(x1-x2), 2) + math.Pow(float64(y1-y2), 2))
}

func main() {
	fmt.Println(maximumDetonation([][]int{{2, 1, 3}, {6, 1, 4}}))                                  // 2
	fmt.Println(maximumDetonation([][]int{{1, 1, 5}, {10, 10, 5}}))                                // 1
	fmt.Println(maximumDetonation([][]int{{1, 2, 3}, {2, 3, 1}, {3, 4, 2}, {4, 5, 3}, {5, 6, 4}})) // 5
}
