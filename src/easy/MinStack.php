<?php

class MinStack {
    private $list;
    private $min;
    /**
     */
    function __construct()
    {
        $this->list = [];
        $this->min = null;
    }

    /**
     * @param Integer $val
     * @return NULL
     */
    function push($val)
    {
        $this->list[] = $val;
        $this->min = is_null($this->min) ? $val : min($this->min, $val);
    }

    /**
     * @return NULL
     */
    function pop()
    {
        $popElement = array_pop($this->list);

        if ($popElement === $this->min) {
            $this->min = $this->list == [] ? null : min($this->list);
        }
    }

    /**
     * @return Integer
     */
    function top()
    {
        return end($this->list);
    }

    /**
     * @return Integer
     */
    function getMin()
    {
        return $this->min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * $obj = MinStack();
 * $obj->push($val);
 * $obj->pop();
 * $ret_3 = $obj->top();
 * $ret_4 = $obj->getMin();
 */