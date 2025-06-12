package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func oddEvenList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	oddHead := &ListNode{Val: head.Val}
	evenHead := head.Next
	evenNode, oddNode := evenHead, oddHead
	for evenNode != nil && evenNode.Next != nil {
		oddNode.Next = evenNode.Next
		evenNode.Next = evenNode.Next.Next
		oddNode = oddNode.Next
		evenNode = evenNode.Next
	}
	oddNode.Next = evenHead
	return oddHead
}
