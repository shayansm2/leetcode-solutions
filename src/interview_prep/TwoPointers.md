# Neetcode questions:

### Two Pointers

| problem                                                                                                  | code                                                                                                  | solution | my notes |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------- | -------- |
| [🟢 Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)                                   | [php](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/easy/ValidPalindrome.php)          |
| [🟡 Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/TwoSumInputArrayIsSorted.go) |
| [🟡 3Sum](https://leetcode.com/problems/3sum/)                                                           | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/3Sum.go)                     |
| [🟡 Container With Most Water](https://leetcode.com/problems/container-with-most-water/)                 |
| [🔴 Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)                             |

---

# Leetcode questions:

### Two Pointers

| problem                                                                                  | code                                                                                                          | solution               | my notes                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 🟢 [Move Zeroes](https://leetcode.com/problems/move-zeroes/)                             | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/easy/MoveZeroesTwoPointer.go)               | slow and fast pointers |
| 🟢 [Is Subsequence](https://leetcode.com/problems/is-subsequence/)                       | [python](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/easy/IsSubsequence.py)                  | slow and fast pointers |
| 🟡 [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/ContainerWithMostWaterTwoPointer.go) | start and end pointers | ⭐⭐⭐ creative solution and beautiful [proof](https://leetcode.com/problems/container-with-most-water/solutions/6099/yet-another-way-to-see-what-happens-in-the-o-n-algorithm/?envType=study-plan-v2&envId=leetcode-75) |

---

### notes:

string manipulations:

```go
package main

import "unicode"

func main() {
	unicode.ToLower('A')  // a
	unicode.IsLetter('$') // false
	unicode.IsDigit('w')  // false
}
```

```python
'#'.isalnum()
'B'.lower()
```
