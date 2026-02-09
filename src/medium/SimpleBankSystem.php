<?php

class Bank
{
    private array $balance;
    private int $n;

    /**
     * @param Integer[] $balance
     */
    function __construct($balance)
    {
        $this->n = count($balance);
        $this->balance = $balance;
    }

    /**
     * @param Integer $account1
     * @param Integer $account2
     * @param Integer $money
     * @return Boolean
     */
    function transfer($account1, $account2, $money)
    {
        if ($account1 < 1 || $account1 > $this->n || $account2 < 1 || $account2 > $this->n) {
            return false;
        }
        if ($this->balance[$account1 - 1] < $money) {
            return false;
        }
        $this->balance[$account1 - 1] -= $money;
        $this->balance[$account2 - 1] += $money;
        return true;
    }

    /**
     * @param Integer $account
     * @param Integer $money
     * @return Boolean
     */
    function deposit($account, $money)
    {
        if ($account < 1 || $account > $this->n) {
            return false;
        }
        $this->balance[$account - 1] += $money;
        return true;
    }

    /**
     * @param Integer $account
     * @param Integer $money
     * @return Boolean
     */
    function withdraw($account, $money)
    {
        if ($account < 1 || $account > $this->n) {
            return false;
        }
        if ($this->balance[$account - 1] < $money) {
            return false;
        }
        $this->balance[$account - 1] -= $money;
        return true;
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * $obj = Bank($balance);
 * $ret_1 = $obj->transfer($account1, $account2, $money);
 * $ret_2 = $obj->deposit($account, $money);
 * $ret_3 = $obj->withdraw($account, $money);
 */
