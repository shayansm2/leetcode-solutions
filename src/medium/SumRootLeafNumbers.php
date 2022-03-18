<?php

class TreeNode
{
    public $val = null;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution
{
    /**
     * @param TreeNode $root
     * @return Integer
     */
    function sumNumbers(TreeNode $root): int
    {
        $stack = [$root];
        $numbers = [$root->val];
        $summation = 0;

        while ($stack) {
            $node = array_pop($stack);
            $currentNumber = array_pop($numbers);
            // echo "DEBUG: we are in node $node->val \n";

            $newNode = null;

            if ($node->left) {
                $newNode = $node->left;
                array_push($stack, $newNode);
                array_push($numbers, $this->calculateNumber($currentNumber, $newNode->val));
            }

            if ($node->right) {
                $newNode = $node->right;
                array_push($stack, $newNode);
                array_push($numbers, $this->calculateNumber($currentNumber, $newNode->val));
            } 
            
            if (is_null($newNode)) {
                // echo "DEBUG: $currentNumber \n";
                $summation += $currentNumber;
            }

            // print_r($numbers);
        }

        return $summation;
    }

    private function calculateNumber($previousNumber, $nodeNumber)
    {
        return 10 * $previousNumber + $nodeNumber;
    }
}

$root = (new TreeNode(1, (new TreeNode(2)), (new TreeNode(3))));
echo (new Solution())->sumNumbers($root);