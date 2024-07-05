package main

import (
	. "leetcode-solutions/src/lib"
)

func main() {
	res := mergeNodes(&ListNode{Next: &ListNode{3, &ListNode{1, &ListNode{0,
		&ListNode{4, &ListNode{5, &ListNode{2, &ListNode{0, nil}}}}}}}})
	res.Show()
}

func mergeNodes(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	var result = &ListNode{Val: 0, Next: nil}
	node := result
	sum := 0

	for head != nil {
		if head.Val == 0 && sum > 0 {
			node.Next = &ListNode{Val: sum, Next: nil}
			node = node.Next
			sum = 0
		} else {
			sum += head.Val
		}
		head = head.Next
	}

	return result.Next
}
