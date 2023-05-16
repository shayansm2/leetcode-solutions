package main

import . "../lib"

func swapPairs(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	newHead := head.Next
	head.Next, newHead.Next = swapPairs(newHead.Next), head
	return newHead
}

func main() {
	list := CreateFromArray([]int{1, 2, 3, 4})
	//list := CreateFromArray([]int{})
	//list := CreateFromArray([]int{1})
	list.Show()
	list = swapPairs(list)
	list.Show()
}
