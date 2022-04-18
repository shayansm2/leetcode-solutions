<?php

class Solution {

    private $nums;
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function singleNonDuplicate(array $nums): int
    {
        $this->nums = $nums;
        return $this->searchForSignleNumber(0, count($nums)); 
    }

    // start is inclusive and end is exclusive
    private function searchForSignleNumber(int $start, int $end): int
    {
        // echo "\nDEBUG $start-$end";
        $middle = intval(($end - $start) / 2) + $start;

        $before = $middle - 1;
        $after = $middle + 1;

        if ($this->nums[$middle] !== $this->nums[$before]
            && $this->nums[$middle] !== $this->nums[$after]) {
                // echo "\nDEBUG FUCK YOU" . $this->nums[$middle];
                return $this->nums[$middle];
        }

        if ($this->nums[$middle] === $this->nums[$before]) {
            if ($before % 2 == 0) {
                return $this->searchForSignleNumber($middle + 1, $end); //right
            }
            
            return $this->searchForSignleNumber($start, $before); //left
        }

        if ($middle % 2 == 0) {
            return $this->searchForSignleNumber($after + 1, $end); //right
        }

        return $this->searchForSignleNumber($start, $middle); //left
    }
}

echo (new Solution())->singleNonDuplicate([3,3,7,7,10,11,11]);