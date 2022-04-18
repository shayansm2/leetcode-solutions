<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function runningSum($nums) {
        $summation = 0;
        $arrayLength = count($nums);
        for ($i = 0; $i < $arrayLength; $i++) {
            $summation += $nums[$i];
            $nums[$i] = $summation;
        }
        return $nums;
    }
}

$examples = [
    ['nums' => [1,2,3,4], 'expectedOutput' =>[1,3,6,10]],
    ['nums' => [1,1,1,1,1], 'expectedOutput' =>[1,2,3,4,5]],
    ['nums' => [3,1,2,10,1], 'expectedOutput' =>[3,4,6,16,17]],
];

foreach ($examples as $example) {
    $nums = $example['nums'];
    $myAnswer = (new Solution())->runningSum($nums);
//    sort($myAnswer);
//    sort($example['expectedOutput']);

    if ($myAnswer != $example['expectedOutput']) {
        print_r($example);
        echo "Your Answer : ";
        print_r($myAnswer);
        echo "\n_____________________________________\n";
    } else {
        echo "\n this test went OK\n";
    }
}