<?php

class ValidPalindrome
{
    /**
     * @param String $s
     * @return Boolean
     */
    function isPalindrome(string $s): bool
    {
        $start = 0;
        $end = strlen($s) - 1;

        while ($start <= $end) {
            while (isset($s[$start]) && !ctype_alnum($s[$start]) && $start <= $end) {
                $start ++;
            }

            while (isset($s[$end]) && !ctype_alnum($s[$end]) && $start <= $end) {
                $end --;
            }

            if ($start > $end) {
                break;
            }

            if (strtolower($s[$start]) != strtolower($s[$end])) {
                return false;
            }

            $start ++;
            $end --;
        }

        return true;
    }
}

echo (new ValidPalindrome())->isPalindrome(" ");