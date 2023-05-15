package main

import (
	"fmt"
	"strconv"
)

// ListNode Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func swapNodes(head *ListNode, k int) *ListNode {
	KthNodePointerFromBeginning := head
	for i := 0; i < k-1; i++ {
		KthNodePointerFromBeginning = KthNodePointerFromBeginning.Next
	}
	// --------------------------------------------------------
	KthNodePointerFromEnd := head
	end := KthNodePointerFromBeginning

	for end.Next != nil {
		KthNodePointerFromEnd = KthNodePointerFromEnd.Next
		end = end.Next
	}
	// --------------------------------------------------------
	KthNodePointerFromBeginning.Val, KthNodePointerFromEnd.Val = KthNodePointerFromEnd.Val, KthNodePointerFromBeginning.Val
	return head
}

func displayLinkedList(head ListNode) {
	representation := ""
	for head.Next != nil {
		representation += strconv.Itoa(head.Val) + "->"
		head = *head.Next
	}
	representation += strconv.Itoa(head.Val)
	fmt.Println(representation)
}

func main() {
	linkedList := ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, &ListNode{5, nil}}}}}
	displayLinkedList(linkedList)
	linkedList = *swapNodes(&linkedList, 2)
	displayLinkedList(linkedList)

	linkedList = ListNode{7, &ListNode{9, &ListNode{6, &ListNode{6, &ListNode{7, &ListNode{8, &ListNode{3, &ListNode{0, &ListNode{9, &ListNode{5, nil}}}}}}}}}}
	displayLinkedList(linkedList)
	linkedList = *swapNodes(&linkedList, 5)
	displayLinkedList(linkedList)
}
