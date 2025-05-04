package main

func reverseList(head *ListNode) *ListNode {
	var result *ListNode = nil
	for head != nil {
		result = &ListNode{Val: head.Val, Next: result}
		head = head.Next
	}
	return result
}
