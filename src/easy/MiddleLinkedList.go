package main

import (
	"fmt"
	. "leetcode-solutions/src/lib"
)

func middleNode(head *ListNode) *ListNode {
	end := head
	middle := head

	for end != nil {
		end = end.Next
		if end == nil {
			break
		}
		end = end.Next
		middle = middle.Next
	}

	return middle
}

func main() {
	fmt.Println(middleNode(&ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, &ListNode{5, nil}}}}}))
	fmt.Println(middleNode(&ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, &ListNode{5, &ListNode{6, nil}}}}}}))
}
