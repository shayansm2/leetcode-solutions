package main

import (
	. "../lib"
	"fmt"
)

func pairSum(head *ListNode) int {
	var tail *ListNode
	n, node := 0, head
	for node != nil {
		tail = &ListNode{Val: node.Val, Next: tail}
		node = node.Next
		n++
	}

	var maxSum int
	for i := 0; i < n/2; i++ {
		if maxSum < head.Val+tail.Val {
			maxSum = head.Val + tail.Val
		}

		head, tail = head.Next, tail.Next
	}

	return maxSum
}

func main() {
	fmt.Println(pairSum(CreateLinkedListFromArray([]int{5, 4, 2, 1})))
	fmt.Println(pairSum(CreateLinkedListFromArray([]int{4, 2, 2, 3})))
	fmt.Println(pairSum(CreateLinkedListFromArray([]int{1, 100000})))
}
