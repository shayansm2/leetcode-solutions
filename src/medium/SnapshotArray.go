package main

import "fmt"

type LinkedListNode struct {
	index int
	value int
	next  *LinkedListNode
}

type SnapshotArray struct {
	roots          []*LinkedListNode
	currents       []*LinkedListNode
	setsInSnapshot []int
	setCounter     int
}

func SnapshotArrayConstructor(length int) SnapshotArray {
	roots := make([]*LinkedListNode, length)
	currents := make([]*LinkedListNode, length)

	for i := 0; i < length; i++ {
		roots[i] = &LinkedListNode{value: 0, index: 0}
	}

	copy(currents, roots[:])

	return SnapshotArray{
		roots:          roots,
		currents:       currents,
		setsInSnapshot: []int{},
		setCounter:     0,
	}
}

func (this *SnapshotArray) Set(index int, val int) {
	this.setCounter++
	node := LinkedListNode{value: val, index: this.setCounter}
	this.currents[index].next = &node
	this.currents[index] = &node
}

func (this *SnapshotArray) Snap() int {
	this.setsInSnapshot = append(this.setsInSnapshot, this.setCounter)
	return len(this.setsInSnapshot) - 1
}

func (this *SnapshotArray) Get(index int, snap_id int) int {
	setIndex := this.setsInSnapshot[snap_id]
	curNode := this.roots[index]
	for {
		if curNode.next == nil {
			break
		}

		if curNode.next.index > setIndex {
			break
		}

		curNode = curNode.next
	}

	return curNode.value
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * obj := SnapshotArrayConstructor(length);
 * obj.Set(index,val);
 * param_2 := obj.Snap();
 * param_3 := obj.Get(index,snap_id);
 */

func main() {
	obj := SnapshotArrayConstructor(3)
	obj.Set(0, 5)
	fmt.Println(obj.Snap())
	obj.Set(0, 6)
	fmt.Println(obj.Get(0, 0))
}
