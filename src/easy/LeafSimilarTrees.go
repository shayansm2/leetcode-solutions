package main

func getLeafs(node *TreeNode) []int {
	if node.Left == nil && node.Right == nil {
		return []int{node.Val}
	}
	if node.Left == nil {
		return getLeafs(node.Right)
	}
	if node.Right == nil {
		return getLeafs(node.Left)
	}
	return append(getLeafs(node.Left), getLeafs(node.Right)...)
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	leafs1 := getLeafs(root1)
	leafs2 := getLeafs(root2)
	if len(leafs1) != len(leafs2) {
		return false
	}
	for i, v1 := range leafs1 {
		if v1 != leafs2[i] {
			return false
		}
	}
	return true
}
