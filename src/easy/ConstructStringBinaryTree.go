package main

import (
	. "leetcode-solutions/src/lib"
	"strconv"
)

func tree2str(root *TreeNode) string {
	var result string
	result += strconv.Itoa(root.Val)

	if root.Left != nil {
		result += "(" + tree2str(root.Left) + ")"
	} else if root.Right != nil {
		result += "()"
	}

	if root.Right != nil {
		result += "(" + tree2str(root.Right) + ")"
	}

	return result
}
