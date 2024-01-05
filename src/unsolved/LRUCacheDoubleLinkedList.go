//package main
//
//import "fmt"
//
//type node struct {
//	prev  *node
//	next  *node
//	value int
//}
//
//type linkedList struct {
//	head *node
//	tail *node
//}
//
//func (this *linkedList) addToHead(value int) {
//	newHead := node{value: value, next: this.head}
//	this.head = &newHead
//
//	if this.tail == nil {
//		this.tail = &node{value: value, prev: this.head}
//	}
//}
//
//func (this *linkedList) addToTail(value int) {
//	newTail := node{value: value, prev: this.tail}
//	this.tail = &newTail
//
//	if this.head == nil {
//		this.head = &newTail
//	}
//}
//
//func (this *linkedList) del(item *node) {
//	item.prev.next = item.next
//	item.next.prev = item.prev
//
//	if this.head == item {
//		this.head = item.next
//	} else if this.tail == item {
//		this.tail = item.prev
//	}
//}
//
//func (this *linkedList) print() {
//	result := ""
//	point := this.head
//	for point != nil {
//		result += string(rune(point.value))
//		point = point.next
//		if point != nil {
//			result += "->"
//		}
//	}
//	fmt.Println(result)
//}
//
//type LRUCache struct {
//	keyValue   map[int]int
//	keyNode    map[int]*node
//	capacity   int
//	linkedList linkedList
//}
//
//func Constructor(capacity int) LRUCache {
//	return LRUCache{
//		keyValue:   map[int]int{},
//		keyNode:    make(map[int]*node),
//		capacity:   capacity,
//		linkedList: linkedList{},
//	}
//}
//
//func (this *LRUCache) Get(key int) int {
//	val, found := this.keyValue[key]
//	if !found {
//		return -1
//	}
//
//	this.linkedList.del(this.keyNode[key])
//	this.linkedList.addToTail(key)
//	this.keyNode[key] = this.linkedList.tail
//
//	this.linkedList.print()
//	return val
//}
//
//func (this *LRUCache) Put(key int, value int) {
//	if prevVal := this.Get(key); prevVal != -1 {
//		this.keyValue[key] = value
//		return
//	}
//
//	if len(this.keyValue) == this.capacity {
//		this.delLRU()
//	}
//
//	this.keyValue[key] = value
//	this.linkedList.addToTail(key)
//	this.keyNode[key] = this.linkedList.tail
//	this.linkedList.print()
//}
//
//func (this *LRUCache) delLRU() {
//	head := this.linkedList.head
//	delete(this.keyValue, head.value)
//	delete(this.keyNode, head.value)
//	this.linkedList.del(head)
//}
//
///**
//* Your LRUCache object will be instantiated and called as such:
//* obj := Constructor(capacity);
//* param_1 := obj.Get(key);
//* obj.Put(key,value);
// */
//
//func main() {
//	lRUCache := Constructor(2)
//	lRUCache.Put(1, 1)           // cache is {1=1}
//	lRUCache.Put(2, 2)           // cache is {1=1, 2=2}
//	fmt.Println(lRUCache.Get(1)) // return 1
//	lRUCache.Put(3, 3)           // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
//	fmt.Println(lRUCache.Get(2)) // returns -1 (not found)
//	lRUCache.Put(4, 4)           // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
//	fmt.Println(lRUCache.Get(1)) // return -1 (not found)
//	fmt.Println(lRUCache.Get(3)) // return 3
//	fmt.Println(lRUCache.Get(4)) // return 4
//
//	lRUCache = Constructor(2)
//	fmt.Println(lRUCache.Get(2))
//	lRUCache.Put(2, 6)
//	fmt.Println(lRUCache.Get(1))
//	lRUCache.Put(1, 5)
//	lRUCache.Put(1, 2)
//	fmt.Println(lRUCache.Get(1))
//	fmt.Println(lRUCache.Get(2))
//}
