<?php

class ListNode 
{
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null)
    {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution 
{
    /**
     * @param ListNode $head
     * @param Integer $val
     * @return ListNode
     */
    function removeElements(ListNode $head, int $val): ListNode 
    {
        if ($head) {
            while ($head->val === $val) {
                $head = $head->next;
            }
        }

        $current = $head;

        while ($current) {
            $next = $current->next;

            if ($next) {
                while ($next->val === $val) {
                    $next = $next->next;
                }
                $current->next = $next;
            }

            $current = $next;
        }

        return $head;
    }
}

// [1,2,6,3,4,5,6]
$seventh = (new ListNode(6));
$sixth = (new ListNode(5, $seventh));
$fifth = (new ListNode(4, $sixth));
$forth = (new ListNode(3, $fifth));
$third = (new ListNode(6, $forth));
$second = (new ListNode(2, $third));
$head = (new ListNode(1, $second));

print_r(
    (new Solution())->removeElements($head, 6)
);