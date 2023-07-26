| problem                                                                                              | code                                                                                                | notes                                                         |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| 🟢 [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)                           | [php](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/easy/ContainsDuplicate.php)      | hash map or hash set                                          |
| 🟢 [Valid Anagram](https://leetcode.com/problems/valid-anagram/)                                     | [py](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/easy/ValidAnagram.py)             | hash map or sort string                                       |
| 🟢 [Two Sum](https://leetcode.com/problems/two-sum/)                                                 | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/easy/TwoSum.go)                   | hash map                                                      |
| 🟡 [Group Anagrams](https://leetcode.com/problems/group-anagrams/)                                   | [py](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/GroupAnagrams.py)          | hash map or sorted string                                     |
| 🟡 [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/KthLargestElementArray.go) | sort or heap queue or quick select or counting (bucket) sort  |
| 🟡 [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)                 | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/TopKFrequentElements.go)   | hash map + heap queue or quick sort or counting (bucket) sort |
| 🟡 [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)       | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/ProductArrayExceptSelf.go) | -                                                             |
| 🟡 [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)                                       | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/ValidSudoku.go)            | -                                                             |
| 🟡 [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)             | [py](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/EncodeDecodeStrings.py)    | encoding and decoding concepts                                |
| 🟡 [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)       |                                                                                                     |                                                               |

covered data structures and algorithms:

1. hash map
2. hash set
3. sorting
4. [heap](https://en.wikipedia.org/wiki/Heap_(data_structure))
5. [quick select](https://en.wikipedia.org/wiki/Quickselect)
6. [quick sort](https://visualgo.net/en/sorting)

---

notes:

#### sorting for arrays with limited value range

- when the range of numbers are limited compared to the count of numbers, instead of sorting the array you can create
  another array with length of all the element's range and put the elements in those (kind of like the bucket sort).

```python
freq = [[] for i in range(len(nums) + 1)]
// instead of sorting the key_value array based on their value
for n, c in key_value.items():
    freq[c].append(n)
```

#### heap queue in go

you can use `container/heap` package for using the heap queue. however you have to implement the heap interface which is
as follows:

```go
package main

import (
	"container/heap"
	"fmt"
)

// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int            { return len(h) }
func (h IntHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func main() {
	// create a new intHeap instance
	nums := &IntHeap{3, 1, 4, 5, 1, 1, 2, 6}

	// The Init function reorders the numbers into a heap
	heap.Init(nums)

	// The slice is now reordered to conform to the heap property
	fmt.Println(nums)

	// Pop the minimum value from the heap
	min := heap.Pop(nums)
	fmt.Println("min: ", min, " heap: ", *nums)
}

```

#### quick sort and random quick sort

both quick sort and quick select use a function named `partition` which takes an index named `pivotIndex`, and returns
the true index of that element.

```
function partition(list, left, right, pivotIndex) is
    pivotValue := list[pivotIndex]
    swap list[pivotIndex] and list[right]  // Move pivot to end
    storeIndex := left
    for i from left to right − 1 do
        if list[i] < pivotValue then
            swap list[storeIndex] and list[i]
            increment storeIndex
    swap list[right] and list[storeIndex]  // Move pivot to its final place
    return storeIndex
```

the difference between quick sort and random quick sort is that the `pivotIndex` in quick sort is the first index of the
array while in random quick sort it's random

```
// Returns the k-th smallest element of list within left..right inclusive
// (i.e. left <= k <= right).
function quickSort(list, left, right) is
    if left = right then   // If the list contains only one element,
        return list[left]  // return that element
    pivotIndex  := ...     // select a pivotIndex between left and right,
                           // e.g., left + floor(rand() % (right − left + 1))
    pivotIndex  := partition(list, left, right, pivotIndex)
    return select(list, left, pivotIndex − 1, k)
    return select(list, pivotIndex + 1, right, k) 
```

#### quick select

it's like quick sort, with the difference that after finding the `pivotIndex`, we only `partition` one of left or right
parts, which we want the kth element to be in

```
// Returns the k-th smallest element of list within left..right inclusive
// (i.e. left <= k <= right).
function select(list, left, right, k) is
    if left = right then   // If the list contains only one element,
        return list[left]  // return that element
    pivotIndex  := ...     // select a pivotIndex between left and right,
                           // e.g., left + floor(rand() % (right − left + 1))
    pivotIndex  := partition(list, left, right, pivotIndex)
    // The pivot is in its final sorted position
    if k = pivotIndex then
        return list[k]
    else if k < pivotIndex then
        return select(list, left, pivotIndex − 1, k)
    else
        return select(list, pivotIndex + 1, right, k) 
```