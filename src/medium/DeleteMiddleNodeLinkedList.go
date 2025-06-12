package main

func deleteMiddle(head *ListNode) *ListNode {
	if head.Next == nil {
		return nil
	}
	endPointer, middlePointer := head, head
	endPointer = endPointer.Next.Next
	for endPointer != nil && endPointer.Next != nil {
		middlePointer = middlePointer.Next
		endPointer = endPointer.Next.Next
	}
	middlePointer.Next = middlePointer.Next.Next
	return head
}
