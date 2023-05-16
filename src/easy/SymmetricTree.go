package main

import . "../lib"

func isSymmetric(root *TreeNode) bool {
	return areInverted(root.Left, root.Right)
}

func areInverted(a *TreeNode, b *TreeNode) bool {
	if a == nil && b == nil {
		return true
	}

	if a == nil || b == nil {
		return false
	}

	if a.Val != b.Val {
		return false
	}

	return areInverted(a.Left, b.Right) && areInverted(a.Right, b.Left)
}
