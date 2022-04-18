<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */

    private $numbers;
    private $target;
    private $startRange = -1;
    private $endRange = -1;

    function searchRange($nums, $target)
    {
        $this->numbers = $nums;
        $this->target = $target;
        $this->searchMultiPosition(0, count($this->numbers));
        return [$this->startRange, $this->endRange];
    }

    private function searchMultiPosition($includedStart, $excludedEnd)
    {
        if ($includedStart >= $excludedEnd) {
            return;
        }

        $middlePoint = floor(($includedStart + $excludedEnd) / 2);

        if ($this->numbers[$middlePoint] === $this->target) {
            $this->startRange = $this->startRange === -1 ? $middlePoint : min($middlePoint, $this->startRange);
            $this->endRange = max($this->endRange, $middlePoint);

            $this->searchMultiPosition($middlePoint + 1, $excludedEnd);
            $this->searchMultiPosition($includedStart, $middlePoint);
            return;
        }

        if ($this->numbers[$middlePoint] < $this->target) {
            $this->searchMultiPosition($middlePoint + 1, $excludedEnd);
            return;
        }
        $this->searchMultiPosition($includedStart, $middlePoint);
    }
}
