package lib

/*
three methods exists for traversing a binary tree which are:
1. Pre-order Traversal (NLR)
2. In-order Traversal (LNR) -> the most common
3. Post-order Traversal (LRN)
each method can be implemented both recursively and iteratively.
*/

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

func visit(visits *[]int, node *TreeNode) {
	*visits = append(*visits, node.Val)
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

func InorderTraversalRecursively(root *TreeNode) []int {
	var visits []int
	inorderTraversalRecursively(root, &visits)
	return visits
}

func inorderTraversalRecursively(node *TreeNode, visits *[]int) {
	if node == nil {
		return
	}

	inorderTraversalRecursively(node.Left, visits)
	visit(visits, node)
	inorderTraversalRecursively(node.Right, visits)
}

//func inorderTraversalIteratively(root *TreeNode) []int {
//}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

func PreorderTraversalRecursively(root *TreeNode) []int {
	var visits []int
	preorderTraversalRecursively(root, &visits)
	return visits
}

func preorderTraversalRecursively(node *TreeNode, visits *[]int) {
	if node == nil {
		return
	}

	visit(visits, node)
	preorderTraversalRecursively(node.Left, visits)
	preorderTraversalRecursively(node.Right, visits)
}

func preorderTraversalIteratively(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	var visits []int
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]

		visits = append(visits, node.Val)

		if node.Left != nil {
			queue = append(queue, node.Left)
		}

		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}

	return visits
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

func PostorderTraversalRecursively(root *TreeNode) []int {
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

//func PostorderTraversalIteratively(root *TreeNode) []int {
//}
