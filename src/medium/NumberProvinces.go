package main

func findCircleNum(isConnected [][]int) int {
	n := len(isConnected)
	var numberOfProvinces int
	visited := make([]bool, n)
	for i := 0; i < n; i++ {
		if visited[i] {
			continue
		}

		numberOfProvinces++
		queue := []int{i}
		for len(queue) > 0 {
			node := queue[0]
			queue = queue[1:]
			if visited[node] {
				continue
			}
			visited[node] = true
			for j, connected := range isConnected[node] {
				if connected == 0 {
					continue
				}
				queue = append(queue, j)
			}
		}
	}
	return numberOfProvinces
}
