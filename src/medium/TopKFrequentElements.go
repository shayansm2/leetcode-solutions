package main

import (
	"container/heap"
	"fmt"
	. "leetcode-solutions/src/lib"
)

//type IntHeap []int
//
//func (heap IntHeap) Len() int           { return len(heap) }
//func (heap IntHeap) Less(i, j int) bool { return heap[i] < heap[j] }
//func (heap IntHeap) Swap(i, j int)      { heap[i], heap[j] = heap[j], heap[i] }
//func (heap *IntHeap) Push(x any)        { *heap = append(*heap, x.(int)) }
//func (heap *IntHeap) Pop() any {
//	old := *heap
//	last := old[heap.Len()-1]
//	*heap = old[:heap.Len()-1]
//	return last
//}

func topKFrequent(nums []int, k int) []int {
	frequency := make(map[int]int)
	for _, num := range nums {
		if _, found := frequency[num]; found {
			frequency[num]++
		} else {
			frequency[num] = 1
		}
	}

	intHeap := IntHeap{}
	heap.Init(&intHeap)
	for _, i := range frequency {
		heap.Push(&intHeap, i)
		if intHeap.Len() > k {
			heap.Pop(&intHeap)
		}
	}

	kthMinVal := heap.Pop(&intHeap).(int)
	var result []int
	for number, freq := range frequency {
		if freq >= kthMinVal {
			result = append(result, number)
		}
	}

	return result
}

func main() {
	fmt.Println(topKFrequent([]int{1, 1, 1, 2, 2, 3}, 2))
	fmt.Println(topKFrequent([]int{1}, 1))
}
