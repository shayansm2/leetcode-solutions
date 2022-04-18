<?php

class FindTownJudge
{
    /**
     * @param Integer $n
     * @param Integer[][] $trust
     * @return Integer
     */
    function findJudge(int $n, array $trust): int
    {
        $getTrust = $setTrust = [];

        for ($i = 1; $i <= $n; $i++) {
            $getTrust[$i] = $setTrust[$i] = 0;
        }

        foreach ($trust as [$setter, $getter]) {
            $setTrust[$setter]++;
            $getTrust[$getter]++;
        }

        for ($i = 1; $i <= $n; $i++) {
            if ($getTrust[$i] == $n - 1 && $setTrust[$i] == 0) {
                return $i;
            }
        }

        return -1;
    }
}