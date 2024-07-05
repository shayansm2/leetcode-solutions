package main

import (
	"fmt"
	. "leetcode-solutions/src/lib"
)

func postorderTraversal(root *TreeNode) []int {
	var visits []int
	postorderTraversalRecursively(root, &visits)
	return visits
}

func postorderTraversalRecursively(node *TreeNode, visits *[]int) {
	if node == nil {
		return
	}

	postorderTraversalRecursively(node.Left, visits)
	postorderTraversalRecursively(node.Right, visits)
	visit(visits, node)
}

func visit(visits *[]int, node *TreeNode) {
	*visits = append(*visits, node.Val)
}

func main() {
	fmt.Println(postorderTraversal(&TreeNode{Val: 1, Right: &TreeNode{Val: 2, Left: &TreeNode{Val: 3}}}))
	fmt.Println(postorderTraversal(nil))
	fmt.Println(postorderTraversal(&TreeNode{Val: 1}))
}
