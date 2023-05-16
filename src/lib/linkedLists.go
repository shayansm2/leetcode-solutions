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

func (head ListNode) Show() {
	representation := ""
	node := head
	for node.Next != nil {
		representation += strconv.Itoa(node.Val) + "->"
		node = *node.Next
	}
	representation += strconv.Itoa(node.Val)
	fmt.Println(representation)
}
