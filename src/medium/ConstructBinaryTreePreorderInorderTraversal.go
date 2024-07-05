package main

import . "leetcode-solutions/src/lib"

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}

	rootIndex := 0
	for inorder[rootIndex] != preorder[0] {
		rootIndex++
	}

	leftPreOrder := preorder[1 : rootIndex+1]
	rightPreOrder := preorder[rootIndex+1:]
	leftInOrder := inorder[:rootIndex]
	rightInOrder := inorder[rootIndex+1:]

	left := buildTree(leftPreOrder, leftInOrder)
	right := buildTree(rightPreOrder, rightInOrder)

	return &TreeNode{Val: preorder[0], Left: left, Right: right}
}
