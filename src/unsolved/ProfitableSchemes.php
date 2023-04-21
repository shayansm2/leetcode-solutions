<?php

class Solution
{
    private array $group;
    private array $profit;

    private array $cache = [];
    private int $modulo = 1000000007;

    /**
     * @param Integer $n
     * @param Integer $minProfit
     * @param Integer[] $group
     * @param Integer[] $profit
     * @return Integer
     */
    function profitableSchemes(int $n, int $minProfit, array $group, array $profit): int
    {
        $this->group = $group;
        $this->profit = $profit;
        return $this->getProfitableSchema($n, $minProfit, count($group) - 1);
    }

    private function getProfitableSchema(int $n, int $minProfit, int $lastCrimeIndex): int
    {
        echo "f($n, $minProfit, $lastCrimeIndex)\n";

        $key = "$n-$minProfit-$lastCrimeIndex";

        if (isset($this->cache[$key])) {
            return $this->cache[$key];
        }

        $result = $this->calculateProfitableSchema($n, $minProfit, $lastCrimeIndex);

        $this->cache[$key] = $result;

        return $result;
    }

    private function calculateProfitableSchema(int $n, int $minProfit, int $lastCrimeIndex): int
    {
        if ($n < 0) {
            return 0;
        }

        if ($lastCrimeIndex < 0) {
            return $minProfit <= 0;
        }

        return ($this->getProfitableSchema(
                    $n - $this->group[$lastCrimeIndex],
                    $minProfit - $this->profit[$lastCrimeIndex],
                    $lastCrimeIndex - 1
                ) % $this->modulo) +
            ($this->getProfitableSchema($n, $minProfit, $lastCrimeIndex - 1) % $this->modulo)
            % $this->modulo;
    }
}

echo (new Solution())->profitableSchemes(n: 5, minProfit: 3, group: [2, 2], profit: [2, 3]);
echo "\n";
echo (new Solution())->profitableSchemes(n: 10, minProfit: 5, group: [2, 3, 5], profit: [6, 7, 8]);
echo "\n";
echo (new Solution())->profitableSchemes(
    n: 100,
    minProfit: 100,
    group: [24, 23, 7, 4, 26, 3, 7, 11, 1, 7, 1, 3, 5, 26, 26, 1, 13, 12, 2, 1, 7, 4, 1, 27, 13, 16, 26, 18, 6, 1, 1, 7, 16, 1, 6, 2, 5, 9, 19, 28, 1, 23, 2, 1, 3, 4, 4, 3, 22, 1, 1, 3, 5, 34, 2, 1, 22, 16, 8, 5, 3, 21, 1, 8, 14, 2, 1, 3, 8, 12, 40, 6, 4, 2, 2, 14, 1, 11, 9, 1, 7, 1, 1, 1, 6, 6, 4, 1, 1, 7, 8, 10, 20, 2, 14, 31, 1, 13, 1, 9],
    profit: [5, 2, 38, 25, 4, 17, 5, 1, 4, 0, 0, 8, 13, 0, 20, 0, 28, 1, 22, 7, 10, 32, 6, 37, 0, 11, 6, 11, 23, 20, 13, 13, 6, 2, 36, 1, 0, 9, 4, 5, 6, 14, 20, 1, 13, 6, 33, 0, 22, 1, 17, 12, 10, 1, 19, 13, 8, 1, 0, 17, 20, 9, 8, 6, 2, 2, 1, 4, 22, 11, 3, 2, 6, 0, 40, 0, 0, 7, 1, 0, 25, 5, 12, 7, 19, 4, 12, 7, 4, 4, 1, 15, 33, 14, 2, 1, 1, 61, 4, 5]
);
echo "\n";