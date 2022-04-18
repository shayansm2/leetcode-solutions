<?php

class LongestSubstringWithoutRepeatingCharacters
{
    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLongestSubstring(string $s): int
    {
        if (strlen($s) === 0) {
            return 0;
        } elseif (strlen($s) === 1) {
            return 1;
        }

        $bestStart = $bestEnd = $lastStart = 0;

        for ($i = 1; $i < strlen($s); $i++) {

            $lastStart = $this->updateLastStart($s, $i, $lastStart);

            if ($i - $lastStart >= $bestEnd - $bestStart) {
                $bestEnd = $i;
                $bestStart = $lastStart;
            }
        }

        return $bestEnd - $bestStart + 1;
    }

    private function updateLastStart(string $s, int $i, int $lastStart): int
    {
        for ($j = $i - 1; $j >= $lastStart; $j--) {
            if ($s[$j] === $s[$i]) {
                return $j + 1;
            }
        }

        return $lastStart;
    }
}
