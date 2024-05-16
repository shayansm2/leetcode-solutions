<?php

class Solution
{

    /**
     * @param String $s
     * @return Integer
     */

    private $s;
    private $length;

    function countBinarySubstrings($s)
    {
        $this->s = $s;
        $this->length = strlen($s);
        $counter = 0;
        // be careful about the for and do not let it to open last char
        $pos = 0;
        while ($pos < $this->length - 1) {
            $lastSamePos = $this->findLastSameChar($pos);
            $lastOppositePos = $this->findLastOppositeChar($lastSamePos, $pos);
            if ($lastOppositePos - $lastSamePos > $lastSamePos - $pos) {
                $counter += ($lastSamePos - $pos + 1);
                $pos = $lastSamePos + 1;
            } else {
                $pos = max([(2 * $lastSamePos) - $lastOppositePos, $pos + 1]);
//                $pos ++;
            }
        }
        return $counter;
    }

    private function findLastSameChar($pos)
    {
        $lastSamePos = $pos;
        while ($lastSamePos < $this->length && $this->s[$lastSamePos] === $this->s[$pos]) {
            $lastSamePos++;
        }
        return --$lastSamePos;
    }

    private function findLastOppositeChar($lastSamePos, $pos)
    {
        $lastOppositePos = $lastSamePos + 1;
//        $lastPosToCheck = $lastOppositePos + $lastSamePos - $pos;
        while (
            $lastOppositePos < $this->length
//            && $lastOppositePos <= $lastPosToCheck
            && $this->s[$lastOppositePos] !== $this->s[$lastSamePos]
        ) {
            $lastOppositePos++;
        }
        return --$lastOppositePos;
    }
}

$tests = [
    "00110011",
    "10101",
    "00110",
];
$s = $tests[4];
//echo substr($s,2205);
echo (new Solution)->countBinarySubstrings($s);