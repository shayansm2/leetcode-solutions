<?php

class FirstBadVersion extends VersionControl
{
    /**
     * @param Integer $n
     * @return Integer
     */
    function firstBadVersion(int $n)
    {
        if ($this->isBadVersion(1)) {
            return 1;
        }

        // assumption is that $from will not be the bad version from now on
        // another assumption is that $to is always a bad version
        return $this->checkBadVersionOfInterval(1, $n);
    }

    private function checkBadVersionOfInterval(int $from, int $to)
    {
        $mid = intval(($from + $to) / 2);

        if ($mid === $from) {
            return $to;
        }

        $isBadVersion = $this->isBadVersion($mid);

        if ($isBadVersion) {
            if ($mid === $from + 1) {
                return $mid;
            }

            return $this->checkBadVersionOfInterval($from, $mid);
        }

        return $this->checkBadVersionOfInterval($mid, $to);
    }
}