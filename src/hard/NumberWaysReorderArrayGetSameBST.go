package main

import (
	"fmt"
	"math/big"
)

const moduloNumOfWays = 1000000007

type BSTNode struct {
	Val   int
	Left  *BSTNode
	Right *BSTNode
}

func numOfWays(nums []int) int {
	root := constructBST(nums)
	result, _ := getNumberOfPermutations(root)
	return result - 1
}

func getNumberOfPermutations(root *BSTNode) (int, int) {
	if root == nil {
		return 1, 0
	}

	if root.Left == nil && root.Right == nil {
		//fmt.Printf("f(%v)=(%v, %v)\n", root.Val, 1, 1)
		return 1, 1
	}

	leftPermutations, leftLen := getNumberOfPermutations(root.Left)
	rightPermutations, rightLen := getNumberOfPermutations(root.Right)
	permutations := ((leftPermutations % moduloNumOfWays) * (rightPermutations % moduloNumOfWays)) % moduloNumOfWays
	coefficient := new(big.Int).Binomial(int64(leftLen+rightLen), int64(leftLen))
	coefficient = new(big.Int).Mod(coefficient, new(big.Int).SetInt64(int64(moduloNumOfWays)))
	permutations = (permutations * int(coefficient.Int64())) % moduloNumOfWays
	//fmt.Printf("f(%v)=(%v, %v)\n", root.Val, permutations, leftLen+rightLen+1)
	return permutations, leftLen + rightLen + 1
}

func constructBST(nums []int) *BSTNode {
	root := &BSTNode{Val: nums[0]}

	for i := 1; i < len(nums); i++ {
		val := nums[i]
		node := root
		for {
			if node.Val < val {
				if node.Right == nil {
					newNode := BSTNode{Val: val}
					node.Right = &newNode
					break
				}
				node = node.Right
			} else {
				if node.Left == nil {
					newNode := BSTNode{Val: val}
					node.Left = &newNode
					break
				}
				node = node.Left
			}
		}
	}

	return root
}

func main() {
	fmt.Println(numOfWays([]int{2, 1, 3}))       // 1
	fmt.Println(numOfWays([]int{3, 4, 5, 1, 2})) // 5
	fmt.Println(numOfWays([]int{1, 2, 3}))       // 0
	//fmt.Println(numOfWays([]int{11, 10, 15, 12, 14, 13})) // 139
	fmt.Println(numOfWays([]int{2, 1, 6, 3, 5, 4}))
	//fmt.Println(numOfWays([]int{9, 7, 11, 8, 10, 15, 12, 14, 13})) // 139
	fmt.Println(numOfWays([]int{3, 1, 5, 2, 4, 9, 6, 8, 7}))                                                                                                                                                                                                                                                                                                                                                     // 139
	fmt.Println(numOfWays([]int{6, 9, 11, 15, 1, 12, 3, 2, 7, 8, 14, 4, 5, 13, 10}))                                                                                                                                                                                                                                                                                                                             //840839
	fmt.Println(numOfWays([]int{19, 3, 57, 34, 15, 89, 58, 35, 2, 33, 46, 13, 40, 79, 60, 30, 61, 26, 54, 22, 84, 51, 75, 6, 87, 44, 55, 48, 27, 8, 72, 47, 16, 69, 36, 76, 41, 1, 80, 62, 73, 24, 93, 50, 92, 65, 39, 5, 32, 67, 12, 29, 90, 45, 9, 38, 88, 52, 10, 85, 74, 66, 83, 18, 20, 77, 49, 28, 23, 53, 86, 64, 78, 82, 37, 42, 56, 17, 81, 4, 14, 70, 59, 31, 7, 25, 43, 68, 91, 71, 21, 63, 94, 11})) // 188718086
}
