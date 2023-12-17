package main

import "fmt"

type MinStack struct {
	last *stackNode
}

type stackNode struct {
	next     *stackNode
	value    int
	minSoFar int
}

func MinStackConstructor() MinStack { return MinStack{last: nil} }

func (this *MinStack) Push(val int) {
	var newNode stackNode

	if this.last == nil {
		newNode = stackNode{
			value:    val,
			minSoFar: val,
		}
	} else {
		newNode = stackNode{
			value:    val,
			next:     this.last,
			minSoFar: min(val, this.last.minSoFar),
		}
	}

	this.last = &newNode
}

func (this *MinStack) Pop() { this.last = this.last.next }

func (this *MinStack) Top() int { return this.last.value }

func (this *MinStack) GetMin() int { return this.last.minSoFar }

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func main() {
	obj := MinStackConstructor()
	obj.Push(-2)
	obj.Push(0)
	obj.Push(-3)
	fmt.Println(obj.GetMin()) // -3
	obj.Pop()
	fmt.Println(obj.Top())    // 0
	fmt.Println(obj.GetMin()) // -2
}
