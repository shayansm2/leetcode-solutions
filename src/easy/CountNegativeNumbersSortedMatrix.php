<?php

class CountNegativeNumbersSortedMatrix
{
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function countNegatives(array $grid): int
    {
        $count = 0;

        $numberOfRows = count($grid);
        $numberOfColumns = count($grid[0]);
        $lastPositiveIndex = $numberOfColumns;

        for ($i = 0; $i < $numberOfRows; $i++) {
            if ($grid[$i][0] < 0) {
                break;
            }

            for ($j = 0; $j < $lastPositiveIndex; $j++) {
                if ($grid[$i][$j] >= 0) {
                    $count ++;
                } else {
                    $lastPositiveIndex = $j;
                    break;
                }
            }
        }

        return ($numberOfColumns * $numberOfRows) - $count;
    }
}