# Data Structures

### Arrays (dynamic array/list)

Given `n = arr.length`

- Add or remove element at the end: `O(1)`
- Add or remove element from arbitrary index: `O(n)`
- Access or modify element at arbitrary index: `O(1)`
- Check if element exists: `O(n)`
- Building a prefix sum: `O(n)`

---

### Strings (immutable)

Given `n = s.length`,

- Add or remove character: `O(n)`
- Access element at arbitrary index: `O(1)`
- Concatenation between two strings: `O(n+m)`
- Create substring: `O(m)`, where m is the length of the substring
- Building a string from joining an array: `O(n)`

---

### Linked Lists

Given `n` as the number of nodes in the linked list,

- Add or remove element given pointer before add/removal location: `O(1)`
- Add or remove element at arbitrary position without pointer: `O(n)`
- Access element at arbitrary position without pointer: `O(n)`
- Check if element exists: `O(n)`

---

### Hash table/dictionary

Given `n = dic.length`,

- Add or remove key-value pair: `O(1)`
- Check if key exists: `O(1)`
- Check if value exists: `O(n)`
- Access or modify value associated with key: `O(1)`
- Iterate over all keys, values, or both: `O(n)`

> Note: the `O(1)` operations are constant relative to `n`. In reality, the hashing algorithm might be expensive. For
> example, if your keys are strings, then it will cost `O(m)` where `m` is the length of the string. The operations
> only take constant time relative to the size of the hash map.

---

### Set

Given `n = set.length`,

- Add or remove element: `O(1)`
- Check if element exists: `O(1)`

> The above note applies here as well.

---

### Stack

Given `n = stack.length`,

- Push element: `O(1)`
- Pop element: `O(1)`
- Peek (see element at top of stack): `O(1)`
- Check if element exists: `O(n)`

[stack implementation](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/lib/stack.py)

---

### Queue

Given `n = queue.length`,

- Enqueue element: `O(1)`
- Dequeue element: `O(1)`
- Peek (see element at front of queue): `O(1)`
- Check if element exists: `O(n)`

[queue implementation](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/lib/queues.py)

---

### Binary search tree

Given `n` as the number of nodes in the tree,

- Add or remove element: `O(n)` worst case, `O(logn)` average case
- Check if element exists: `O(n)` worst case, `O(logn)` average case

The average case is when the tree is well-balanced - each depth is close to full. The worst case is when the tree is
just a straight line.

[binary tree implementation](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/lib/binaryTree.py)

---

### Heap/Priority Queue

Given `n = heap.length` and talking about min heaps,

- Add an element: `O(logn)`
- Delete the minimum element: `O(logn)`
- Find the minimum element: `O(1)`
- Check if element exists: `O(n)`

[heap implementation](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/lib/heap.py)

---

resources:
- [leetcode cheatsheet](https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4725/)
- [quera algorithm course](https://quera.org/college/landpage/3016/Data-Structures-and-Algorithmic-Thinking)