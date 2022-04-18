<?php

class HappyNumber
{
    /**
     * @param Integer $n
     * @return Boolean
     */
    function isHappy(int $n): bool
    {
        $history = [];

        while ($n !== 1) {
            $history[] = $n;

            $n = $this->calculateNewN($n);

            if (in_array($n, $history)) {
                return false;
            }
        }

        return true;
    }

    private function calculateNewN(int $n): int
    {
        $newN = 0;

        while ($n !== 0) {
            $lastDigit = $n % 10;
            $n = intval($n/10);

            $newN += ($lastDigit ** 2);
        }

        return $newN;
    }
}
