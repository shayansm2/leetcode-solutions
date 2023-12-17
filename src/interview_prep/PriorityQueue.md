# my selected questions

### Heap / Priority Queue

| problem                                                                                      | code                                                                                                | solutions | my notes |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------|----------|
| 🟡 [Design a Food Rating System](https://leetcode.com/problems/design-a-food-rating-system/) | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/DesignFoodRatingSystem.go) |
| 🟡 [LRU Cache](https://leetcode.com/problems/lru-cache/)                                     |                                                                                                     |

### notes:

- [implementation of heap in go](../lib/heap.go)
- heaps are a good data structure when we want to find the minimum or maximum of a stream of data in low
  time `O(1) for getting min/max`.
- However, keeping the heap update may be challenging when the value of each data changes over
  time `O(n) for searching for a value and O(logn) for replacing it`
- one way of handling this is to not keep the heap inconsistent with the old data and check it when the min/max is being
  retrieved.