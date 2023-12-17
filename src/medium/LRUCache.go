package main

import (
	"container/heap"
	"fmt"
)

type callStat struct {
	counter int
	key     int
}

type callStatHeap []callStat

func (h callStatHeap) Len() int            { return len(h) }
func (h callStatHeap) Less(i, j int) bool  { return h[i].counter < h[j].counter }
func (h callStatHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *callStatHeap) Push(x interface{}) { *h = append(*h, x.(callStat)) }
func (h *callStatHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type LRUCache struct {
	keyValueStore map[int]int
	callHistory   map[int]int
	callCounter   int
	minHeap       callStatHeap
	capacity      int
}

func Constructor(capacity int) LRUCache {
	minHeap := make(callStatHeap, 0)
	heap.Init(&minHeap)
	return LRUCache{
		keyValueStore: make(map[int]int),
		callHistory:   make(map[int]int),
		callCounter:   0,
		minHeap:       minHeap,
		capacity:      capacity,
	}
}

func (this *LRUCache) Get(key int) int {
	this.callCounter++

	value, found := this.keyValueStore[key]
	if !found {
		return -1
	}

	this.callHistory[key] = this.callCounter

	stat := callStat{
		counter: this.callCounter,
		key:     key,
	}

	heap.Push(&this.minHeap, stat)

	return value
}

func (this *LRUCache) Put(key int, value int) {
	this.callCounter++

	this.keyValueStore[key] = value
	this.callHistory[key] = this.callCounter

	stat := callStat{
		counter: this.callCounter,
		key:     key,
	}

	heap.Push(&this.minHeap, stat)

	if len(this.keyValueStore) > this.capacity {
		delKey := this.findDeleteKey()
		this.del(delKey)
	}
}

func (this *LRUCache) findDeleteKey() int {
	for {
		minItem := heap.Pop(&this.minHeap).(callStat)
		accurateCounter, found := this.callHistory[minItem.key]
		if found && minItem.counter == accurateCounter {
			heap.Push(&this.minHeap, minItem)
			return minItem.key
		}
	}
}

func (this *LRUCache) del(key int) {
	delete(this.keyValueStore, key)
	delete(this.callHistory, key)
}

func main() {
	lRUCache := Constructor(2)
	lRUCache.Put(1, 1)           // cache is {1=1}
	lRUCache.Put(2, 2)           // cache is {1=1, 2=2}
	fmt.Println(lRUCache.Get(1)) // return 1
	lRUCache.Put(3, 3)           // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
	fmt.Println(lRUCache.Get(2)) // returns -1 (not found)
	lRUCache.Put(4, 4)           // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
	fmt.Println(lRUCache.Get(1)) // return -1 (not found)
	fmt.Println(lRUCache.Get(3)) // return 3
	fmt.Println(lRUCache.Get(4)) // return 4

	lRUCache = Constructor(2)
	fmt.Println(lRUCache.Get(2))
	lRUCache.Put(2, 6)
	fmt.Println(lRUCache.Get(1))
	lRUCache.Put(1, 5)
	lRUCache.Put(1, 2)
	fmt.Println(lRUCache.Get(1))
	fmt.Println(lRUCache.Get(2))
}
