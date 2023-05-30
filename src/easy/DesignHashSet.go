package main

import "fmt"

type MyHashSet struct {
	hashMap map[int]bool
}

func Constructor() MyHashSet {
	hashMap := make(map[int]bool)
	return MyHashSet{hashMap: hashMap}
}

func (this *MyHashSet) Add(key int) {
	this.hashMap[key] = true
}

func (this *MyHashSet) Remove(key int) {
	this.hashMap[key] = false
}

func (this *MyHashSet) Contains(key int) bool {
	return this.hashMap[key] == true
}

func main() {
	obj := Constructor()
	obj.Add(1)
	obj.Add(2)
	fmt.Println(obj.Contains(1))
	fmt.Println(obj.Contains(3))
	obj.Add(2)
	fmt.Println(obj.Contains(2))
	obj.Remove(2)
	fmt.Println(obj.Contains(2))
}
