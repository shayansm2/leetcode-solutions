package main

import . "../lib"

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

func main() {
	linkedList := ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5}}}}}
	linkedList.Show()
	linkedList = *swapNodes(&linkedList, 2)
	linkedList.Show()

	linkedList = ListNode{Val: 7, Next: &ListNode{Val: 9, Next: &ListNode{Val: 6, Next: &ListNode{Val: 6, Next: &ListNode{Val: 7, Next: &ListNode{Val: 8, Next: &ListNode{Val: 3, Next: &ListNode{Next: &ListNode{Val: 9, Next: &ListNode{Val: 5}}}}}}}}}}
	linkedList.Show()
	linkedList = *swapNodes(&linkedList, 5)
	linkedList.Show()
}
