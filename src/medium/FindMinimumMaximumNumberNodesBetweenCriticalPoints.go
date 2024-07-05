package main

import . "leetcode-solutions/src/lib"

func nodesBetweenCriticalPoints(head *ListNode) []int {
	var index = 1
	var firstCriticalPointIndex int
	var previousCriticalPointIndex int
	var currentCriticalPointIndex int
	var minDistance = -1
	var prevNode *ListNode

	for head != nil {
		if prevNode != nil && head.Next != nil {
			isCriticalPoint := head.Val < head.Next.Val && head.Val < prevNode.Val
			isCriticalPoint = isCriticalPoint || (head.Val > head.Next.Val && head.Val > prevNode.Val)
			if isCriticalPoint {
				if firstCriticalPointIndex == 0 {
					firstCriticalPointIndex = index
				}

				previousCriticalPointIndex = currentCriticalPointIndex
				currentCriticalPointIndex = index

				if minDistance == -1 && previousCriticalPointIndex != 0 {
					minDistance = currentCriticalPointIndex - previousCriticalPointIndex
				}

				if minDistance > currentCriticalPointIndex-previousCriticalPointIndex {
					minDistance = currentCriticalPointIndex - previousCriticalPointIndex
				}
			}
		}

		index++
		prevNode = head
		head = head.Next
	}

	maxDistance := -1
	if minDistance != -1 {
		maxDistance = currentCriticalPointIndex - firstCriticalPointIndex
	}
	return []int{minDistance, maxDistance}
}
