<?php


class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function containsDuplicate($nums) {
        $array = [];

        foreach ($nums as $number) {
            if (isset($array[$number])) {
                return true;
            }

            $array[$number] = $number;
        }

        return false;
    }
}