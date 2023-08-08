# Neetcode questions:

### Two Pointers

| problem                                                                                                  | code                                                                                                | solution | my notes |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|----------|----------|
| [🟢 Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)                                   | [php](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/easy/ValidPalindrome.php)        |
| [🟡 Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/easy/TwoSumInputArrayIsSorted.go) |
| [🟡 3Sum](https://leetcode.com/problems/3sum/)                                                           |
| [🟡 Container With Most Water](https://leetcode.com/problems/container-with-most-water/)                 |
| [🔴 Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)                             |

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