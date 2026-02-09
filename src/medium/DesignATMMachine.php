<?php

class ATM
{
    private array $banknotes;
    private const VALUES = [20, 50, 100, 200, 500];

    /**
     */
    function __construct()
    {
        $this->banknotes = [0, 0, 0, 0, 0];
    }

    /**
     * @param Integer[] $banknotesCount
     * @return NULL
     */
    function deposit($banknotesCount)
    {
        foreach ($banknotesCount as $i => $banknoteCount) {
            $this->banknotes[$i] += $banknoteCount;
        }
    }

    /**
     * @param Integer $amount
     * @return Integer[]
     */
    function withdraw($amount)
    {
        $result = [0, 0, 0, 0, 0];
        foreach (array_reverse($this->banknotes, true) as $i => $banknote) {
            // echo "DEBUG: we are in banknote $i : $banknote \n";
            if ($amount == 0) {
                break;
            }

            // echo "DEBUG: value is " . self::VALUES[$i] . "\n";

            if ($banknote > 0 && $amount >= self::VALUES[$i]) {
                $count =  min(intval($amount / self::VALUES[$i]), $banknote);
                // echo "DEBUG: count is $count";
                $amount -= ($count * self::VALUES[$i]);
                $result[$i] = $count;
            }
        }

        if ($amount != 0) {
            return [-1];
        }
        foreach ($result as $i => $banknoteCount) {
            $this->banknotes[$i] -= $banknoteCount;
        }
        return $result;
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * $obj = ATM();
 * $obj->deposit($banknotesCount);
 * $ret_2 = $obj->withdraw($amount);
 */
$atm = new ATM();
$atm->deposit([0, 0, 1, 2, 1]);
print_r($atm->withdraw(600));
$atm->deposit([0, 1, 0, 1, 1]);
print_r($atm->withdraw(600));
print_r($atm->withdraw(550));
