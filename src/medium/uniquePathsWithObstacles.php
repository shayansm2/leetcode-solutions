<?php

class Solution
{

    /**
     * @param Integer[][] $obstacleGrid
     * @return Integer
     */
    function uniquePathsWithObstacles($obstacleGrid)
    {
        // maskhare bazi
        if ($obstacleGrid[0][0] === 1) {
            return 0;
        }

        $firstRow = $obstacleGrid[0];
        $numberOfColumns = count($firstRow);
        $numberOfRows = count($obstacleGrid);

        // maskhare bazi
        if ($obstacleGrid[$numberOfRows-1][$numberOfColumns-1] === 1) {
            return 0;
        }

        $uniquePaths = [];
        foreach ($firstRow as $index => $item) {
            $uniquePaths[] = $item ? 0 :
                (!$index ? 1 : $uniquePaths[$index-1]);
        }
        $uniquePaths = [$uniquePaths];

        for ($rowNumber = 1; $rowNumber < $numberOfRows; $rowNumber ++) {
            $uniquePaths[] = [];
            for ($columnNumber = 0; $columnNumber < $numberOfColumns; $columnNumber ++) {
                if ($obstacleGrid[$rowNumber][$columnNumber] === 1) {
                    $uniquePaths[$rowNumber][] = 0;
                } else if ($columnNumber === 0) {
                    $uniquePaths[$rowNumber][] = $uniquePaths[$rowNumber-1][$columnNumber];
                } else {
                    $uniquePaths[$rowNumber][] =
                        $uniquePaths[$rowNumber][$columnNumber-1] +
                        $uniquePaths[$rowNumber-1][$columnNumber];
                }
            }
        }

        return $uniquePaths[$numberOfRows-1][$numberOfColumns-1];

    }
}

$obstacleGrids = [
    [[0, 0, 0, 1], [0, 1, 0, 1], [0, 1, 0, 0]],
    [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
    [[0, 1], [0, 0]],
    [[1,0]],
    [[0,0],[1,1],[0,0]],
    [[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
];

foreach ($obstacleGrids as $obstacleGrid) {
    print_r((new Solution())->uniquePathsWithObstacles($obstacleGrid));
    echo "\n";
}
