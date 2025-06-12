package main

func updateCount(node *TrieTree, maxSoFar int, count *int) {
	if node.Val >= maxSoFar {
		*count++
		maxSoFar = node.Val
	}
	if node.Left != nil {
		updateCount(node.Left, maxSoFar, count)
	}
	if node.Right != nil {
		updateCount(node.Right, maxSoFar, count)
	}
}

func goodNodes(root *TreeNode) int {
	count := 0
	updateCount(root, root.Val, &count)
	return count
}
