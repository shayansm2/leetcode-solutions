package main

import (
	. "../lib"
)

func maxLevelSum(root *TreeNode) int {
	nodeQueue, levelQueue := []*TreeNode{root}, []int{1}
	curLevel, levelSum, maxSum, result := 1, 0, 0, 0

	for len(nodeQueue) > 0 {
		node, level := nodeQueue[0], levelQueue[0]
		nodeQueue, levelQueue = nodeQueue[1:], levelQueue[1:]

		if node.Left != nil {
			nodeQueue = append(nodeQueue, node.Left)
			levelQueue = append(levelQueue, level+1)
		}

		if node.Right != nil {
			nodeQueue = append(nodeQueue, node.Right)
			levelQueue = append(levelQueue, level+1)
		}

		if level != curLevel {
			if maxSum < levelSum || curLevel == 1 {
				maxSum = levelSum
				result = curLevel
			}
			levelSum = 0
			curLevel = level
		}
		levelSum += node.Val
	}

	if maxSum < levelSum {
		maxSum = levelSum
		result = curLevel
	}

	return result
}
