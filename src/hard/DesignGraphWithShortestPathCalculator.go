package main

import (
	"container/heap"
	"fmt"
)

func main() {
	test1()
}

func test1() {
	graph := Constructor(4, [][]int{{0, 2, 5}, {0, 1, 2}, {1, 2, 1}, {3, 0, 3}})
	fmt.Println(graph)
	fmt.Println(graph.ShortestPath(3, 2), 6)
	fmt.Println(graph.ShortestPath(0, 3), -1)
	graph.AddEdge([]int{1, 3, 4})
	fmt.Println(graph.ShortestPath(0, 3), 6)
}

type Edge struct {
	to       int
	distance int
}

type Graph struct {
	nodes map[int][]Edge
}

func Constructor(n int, edges [][]int) Graph {
	nodes := make(map[int][]Edge)
	for i := 0; i < n; i++ {
		nodes[i] = make([]Edge, 0)
	}
	graph := Graph{nodes: nodes}
	for _, edge := range edges {
		graph.AddEdge(edge)
	}
	return graph
}

func (this *Graph) AddEdge(edge []int) {
	this.nodes[edge[0]] = append(this.nodes[edge[0]], Edge{to: edge[1], distance: edge[2]})
}

type nodeStat struct {
	nodeId   int
	distance int
}

type nodeStatHeap []nodeStat

func (this *nodeStatHeap) Len() int {
	return len(*this)
}

func (this *nodeStatHeap) Less(i, j int) bool {
	return (*this)[i].distance < (*this)[j].distance
}

func (this *nodeStatHeap) Swap(i, j int) {
	(*this)[i], (*this)[j] = (*this)[j], (*this)[i]
}

func (this *nodeStatHeap) Push(x any) {
	*this = append(*this, x.(nodeStat))
}

func (this *nodeStatHeap) Pop() any {
	newThis := (*this)[:len(*this)-1]
	pop := (*this)[len(*this)-1]
	*this = newThis
	return pop
}

func (this *Graph) ShortestPath(node1 int, node2 int) int {
	nodeStats := make(nodeStatHeap, 0)
	nodeStats = append(nodeStats, nodeStat{nodeId: node1, distance: 0})
	heap.Init(&nodeStats)

	visited := make(map[int]bool)
	visited[node1] = true
	for len(nodeStats) > 0 {
		node := heap.Pop(&nodeStats).(nodeStat)
		visited[node.nodeId] = true
		if node.nodeId == node2 {
			return node.distance
		}

		for _, neighbour := range this.nodes[node.nodeId] {
			if _, found := visited[neighbour.to]; found {
				continue
			}
			heap.Push(&nodeStats, nodeStat{nodeId: neighbour.to, distance: node.distance + neighbour.distance})
		}
	}
	return -1
}
