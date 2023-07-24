package lib

import (
	"container/heap"
	"fmt"
)

// An IntHeap is a min-heap of ints.
type IntHeap []int

// sort interface
func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

// heap interface
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func main() {
	// create a new intHeap instance
	nums := &IntHeap{3, 1, 4, 5, 1, 1, 2, 6}

	// The Init function reorders the numbers into a heap
	heap.Init(nums)

	// The slice is now reordered to conform to the heap property
	fmt.Println(nums)

	// Pop the minimum value from the heap
	min := heap.Pop(nums)
	heap.Push(nums, 3)
	fmt.Println("min: ", min, " heap: ", *nums)
}
