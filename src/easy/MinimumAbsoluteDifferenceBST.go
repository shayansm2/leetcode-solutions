package main

import (
	"fmt"
	. "leetcode-solutions/src/lib"
)

type TreeNodeStat struct {
	minDiff int
	min     int
	max     int
}

func getMinimumDifference(root *TreeNode) int {
	return getTreeNodeStat(root).minDiff
}

func getTreeNodeStat(node *TreeNode) TreeNodeStat {
	stat := TreeNodeStat{min: node.Val, max: node.Val, minDiff: 100001}

	if node.Left != nil {
		leftStat := getTreeNodeStat(node.Left)
		stat.min = leftStat.min

		if leftStat.minDiff < stat.minDiff {
			stat.minDiff = leftStat.minDiff
		}

		if node.Val-leftStat.max < stat.minDiff {
			stat.minDiff = node.Val - leftStat.max
		}
	}

	if node.Right != nil {
		rightStat := getTreeNodeStat(node.Right)
		stat.max = rightStat.max

		if rightStat.minDiff < stat.minDiff {
			stat.minDiff = rightStat.minDiff
		}

		if rightStat.min-node.Val < stat.minDiff {
			stat.minDiff = rightStat.min - node.Val
		}
	}

	return stat
}

func main() {
	fmt.Println(
		getMinimumDifference(
			&TreeNode{
				Val: 4,
				Left: &TreeNode{
					Val:   2,
					Left:  &TreeNode{Val: 1},
					Right: &TreeNode{Val: 3},
				},
				Right: &TreeNode{Val: 6},
			}))
}
