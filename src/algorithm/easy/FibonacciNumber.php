<?php

class FibonacciNumber
{
    /**
     * @param Integer $n
     * @return Integer
     */
    function fib($n)
    {
        if ($n < 2) {
            return 1;
        }

        $fibArray = [];
        $fibArray[0] = 0;
        $fibArray[1] = 1;

        for ($i = 2; $i <= $n; $i++) {
            $fibArray[$i] = $fibArray[$i-1] + $fibArray[$i-2];
        }

        return $fibArray[$n];
    }
}