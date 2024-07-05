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

func CreateLinkedListFromArrayReverse(array []int) *ListNode {
	var curNode *ListNode = nil
	for i := len(array) - 1; i >= 0; i-- {
		curNode = &(ListNode{Val: array[i], Next: curNode})
	}
	return curNode
}

func CreateLinkedListFromArrayStraight(array []int) *ListNode {
	if len(array) == 0 {
		return nil
	}

	result := &ListNode{array[0], nil}
	current := result

	for i := 1; i < len(array); i++ {
		current.Next = &ListNode{array[i], nil}
		current = current.Next
	}

	return result
}
