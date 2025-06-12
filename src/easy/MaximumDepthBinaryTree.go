package main

func updateMaxDepth(node *TreeNode, curDepth int, maxDepth *int) {
	*maxDepth = max(*maxDepth, curDepth)
	if node.Left != nil {
		updateMaxDepth(node.Left, curDepth+1, maxDepth)
	}
	if node.Right != nil {
		updateMaxDepth(node.Right, curDepth+1, maxDepth)
	}
}

func maxDepth(root *TreeNode) int {
	result := 0
	if root != nil {
		updateMaxDepth(root, 1, &result)
	}
	return result
}
