<?php

class Solution
{

    /**
     * @param Integer $x
     * @param Integer $y
     * @param Integer $bound
     * @return Integer[]
     */
    function powerfulIntegers($x, $y, $bound)
    {
        $powerfulIntegers =[];
        $i = 0;
        while (pow($x, $i) <= $bound) {
            $j = 0;
            while (pow($x, $i) + pow($y, $j) <= $bound) {
                $powerfulInteger = pow($x, $i) + pow($y, $j);
                $powerfulIntegers[$powerfulInteger] = $powerfulInteger;
                if ($y === 1) {
                    break;
                }
                $j ++;
            }
            if ($x === 1) {
                break;
            }
            $i ++;
        }
        return array_values($powerfulIntegers);
    }

}

$examples = [
    ['x' => 2, 'y' => 3, 'bound' => 10, 'expectedOutput' => [2, 3, 4, 5, 7, 9, 10]],
    ['x' => 3, 'y' => 5, 'bound' => 15, 'expectedOutput' => [2, 4, 6, 8, 10, 14]],
    ['x' => 2, 'y' => 1, 'bound' => 10, 'expectedOutput' => [9,2,3,5]],
    ['x' => 1, 'y' => 1, 'bound' => 0, 'expectedOutput' => []],
    ['x' => 60, 'y' => 56, 'bound' => 175617, 'expectedOutput' => [175617,2,3137,3656,6736,3601,116,57,3196,61]],
];

foreach ($examples as $example) {
    $x = $example['x'];
    $y = $example['y'];
    $bound =  $example['bound'];
    $myAnswer = (new Solution())->powerfulIntegers($x, $y, $bound);
    sort($myAnswer);
    sort($example['expectedOutput']);

    if ($myAnswer != $example['expectedOutput']) {
        print_r($example);
        echo "Your Answer : ";
        print_r($myAnswer);
        echo "\n_____________________________________\n";
    } else {
        echo "\n this test went OK\n";
    }
}