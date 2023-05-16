package lib

import (
	"fmt"
	"strconv"
)

// ListNode Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func (head *ListNode) Show() {
	if head == nil {
		fmt.Println("Empty ListNode")
		return
	}
	representation := ""
	node := head
	for node.Next != nil {
		representation += strconv.Itoa(node.Val) + "->"
		node = node.Next
	}
	representation += strconv.Itoa(node.Val)
	fmt.Println(representation)
}

func CreateFromArray(array []int) *ListNode {
	var curNode *ListNode = nil
	for i := len(array) - 1; i >= 0; i-- {
		curNode = &(ListNode{Val: array[i], Next: curNode})
	}
	return curNode
}
