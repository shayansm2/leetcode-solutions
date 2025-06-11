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
| 🟡 [Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/MaxNumberKSumPairs.go)               | start and end pointer  | like "two sum" problem                                                                                                                                                                                                   |

### Sliding Window

| problem                                                                                                                                                   | code                                                                                                                     | solution | my notes                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------- | -------------------------------------------------- |
| 🟢 [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)                                                                | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/easy/MaximumAverageSubarrayI.go)                       |
| 🟡 [1456-Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | [python](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/MaximumNumberVowelsSubstringGivenLength.py) |
| 🟡 [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)                                                                    | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/MaxConsecutiveOnesIII.go)                       |
| 🟡 [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)                 | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/LongestSubarray1AfterDeletingOneElement.go)     |          | very similar to "Max Consecutive Ones III" problem |

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
