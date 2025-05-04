package main

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	var result *ListNode = &ListNode{Val: -1, Next: nil}
	node := result
	for list1 != nil || list2 != nil {
		if list1 == nil {
			node.Next = list2
			return result.Next
		}
		if list2 == nil {
			node.Next = list1
			return result.Next
		}
		if list1.Val <= list2.Val {
			node.Next = &ListNode{Val: list1.Val}
			list1 = list1.Next
		} else {
			node.Next = &ListNode{Val: list2.Val}
			list2 = list2.Next
		}
		node = node.Next
	}
	return result.Next
}
