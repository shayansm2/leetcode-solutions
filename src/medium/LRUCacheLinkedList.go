package main

import (
	"container/list"
	"fmt"
)

type LRUCache struct {
	keyValue   map[int]int
	keyNode    map[int]*list.Element
	capacity   int
	linkedList *list.List
}

func LRUCacheConstructor(capacity int) LRUCache {
	return LRUCache{
		keyValue:   map[int]int{},
		keyNode:    make(map[int]*list.Element),
		capacity:   capacity,
		linkedList: list.New(),
	}
}

func (this *LRUCache) Get(key int) int {
	val, found := this.keyValue[key]
	if !found {
		return -1
	}

	this.linkedList.Remove(this.keyNode[key])
	this.linkedList.PushFront(key)
	this.keyNode[key] = this.linkedList.Front()

	return val
}

func (this *LRUCache) Put(key int, value int) {
	if prevVal := this.Get(key); prevVal != -1 {
		this.keyValue[key] = value
		return
	}

	if len(this.keyValue) == this.capacity {
		this.delLRU()
	}

	this.keyValue[key] = value
	this.linkedList.PushFront(key)
	this.keyNode[key] = this.linkedList.Front()
}

func (this *LRUCache) delLRU() {
	head := this.linkedList.Back()
	delete(this.keyValue, head.Value.(int))
	delete(this.keyNode, head.Value.(int))
	this.linkedList.Remove(head)
}

/**
* Your LRUCache object will be instantiated and called as such:
* obj := Constructor(capacity);
* param_1 := obj.Get(key);
* obj.Put(key,value);
 */

func main() {
	lRUCache := LRUCacheConstructor(2)
	lRUCache.Put(1, 1)           // cache is {1=1}
	lRUCache.Put(2, 2)           // cache is {1=1, 2=2}
	fmt.Println(lRUCache.Get(1)) // return 1
	lRUCache.Put(3, 3)           // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
	fmt.Println(lRUCache.Get(2)) // returns -1 (not found)
	lRUCache.Put(4, 4)           // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
	fmt.Println(lRUCache.Get(1)) // return -1 (not found)
	fmt.Println(lRUCache.Get(3)) // return 3
	fmt.Println(lRUCache.Get(4)) // return 4

	lRUCache = LRUCacheConstructor(2)
	fmt.Println(lRUCache.Get(2))
	lRUCache.Put(2, 6)
	fmt.Println(lRUCache.Get(1))
	lRUCache.Put(1, 5)
	lRUCache.Put(1, 2)
	fmt.Println(lRUCache.Get(1))
	fmt.Println(lRUCache.Get(2))
}
