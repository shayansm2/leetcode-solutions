<?php

class Solution {

/**
 * @param Integer[][] $wall
 * @return Integer
 */
    function leastBricks($wall) {
     
        $wallCumSum = [];
        $mostFrequent = [];
        foreach($wall as $row) {
            $cumSum = 0;
            $rowCumSum = [];
            foreach($row as $brick) {
                $cumSum += $brick;
                if(key_exists($cumSum, $mostFrequent)) {
                    $mostFrequent[$cumSum] ++;
                } else {
                    $mostFrequent[$cumSum] = 1;
                }
                $rowCumSum[] = $cumSum;
            }
            $wallCumSum[] = $rowCumSum;
        }

        unset($mostFrequent[$cumSum]);

        if(empty($mostFrequent)) {
            return count($wall);
        }

        $bestLine = array_keys($mostFrequent, max($mostFrequent))[0];

        $counter = 0;
        foreach($wallCumSum as $rowCumSum) {
            if(!in_array($bestLine, $rowCumSum)) {
                $counter ++;
            }
        }

        return $counter;

    }
}


$wall = 
// [[100000000],[100000000],[100000000]];
[[1,2,2,1],
[3,1,2],
[1,3,2],
[2,4],
[3,1,2],
[1,3,1,1]];

print_r(Solution::leastBricks($wall));