# Neetcode questions:

### stacks

| problem                                                                                                | code                                                                                                       | solution                                                              | my notes                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🟢 [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)                               | [js](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/easy/ValidParentheses.js)                | stack                                                                 | could have added termination logics                                                                                                                                                                                                                                                               |
| 🟡 [Min Stack](https://leetcode.com/problems/min-stack/)                                               | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/MinStack.go)                      | stack                                                                 | min/max of a stack can stays in the last node `implementation`                                                                                                                                                                                                                                    |
| 🟡 [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/EvaluateReversePolishNotation.go) | stack                                                                 | advantage of reverse Polish notation is that it removes the need for order of operations and parentheses that are required by infix notation and can be evaluated linearly                                                                                                                        |
| 🟡 [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)                         | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/GenerateParentheses.go)           | backtracking, recursion                                               | ⭐⭐                                                                                                                                                                                                                                                                                              |
| 🟢 [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)                     | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/NextGreaterElementI.go)           | monotonic stack (_find the next greater element_)                     |                                                                                                                                                                                                                                                                                                   |
| 🟡 [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)                   | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/NextGreaterElementII.go)          | monotonic stack (_find the next greater element_)                     |                                                                                                                                                                                                                                                                                                   |
| 🟡 [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)                             | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/DailyTemperatures.go)             | monotonic stack (_find the next day with greater temperature_)        | ⭐                                                                                                                                                                                                                                                                                                |
| 🟡 [Car Fleet](https://leetcode.com/problems/car-fleet/)                                               | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/CarFleet.go)                      | array(`o(n2)`), monotonic stack (_find the next slower cat_) (`o(n)`) | ⭐ mathematical thinking behind this question was the important part, not the data structures and algorithms, creative solution <br> 1. look for car collisions (comparing each two points with one another) <br> 2. look for time arrival of each car (comparing each node with one source node) |
| 🟡 [Remove K Digits](https://leetcode.com/problems/remove-k-digits/)                                   | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/RemoveKDigits.go)                 | monotonic stack (_find the prev smaller digit_)                       | ⭐⭐ full of edge cases                                                                                                                                                                                                                                                                           |
| 🔴 [Largest Rectangle In Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)     | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/hard/LargestRectangleHistogram.go)       | monotonic stack (_find the prev and next smaller number_)             | ⭐⭐ 1. looking for start and end indices and calculate the area <br> 2. looking for max length containing the start index <br> 3. looking for max length containing the index                                                                                                                    |

# Leetcode questions:

### stacks

| problem                                                                                        | code                                                                                                         | solution | my notes |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------- | -------- |
| 🟡 [Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/) | [javascript](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/RemovingStarsFromString.js) |
| 🟡 [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)                     | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/AsteroidCollision.go)               |

### Queues

| problem                                                                            | code                                                                                         | solution                                                                                                                              | my notes |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 🟢 [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/easy/NumberRecentCalls.go) |
| 🟡 [Dota2 Senate](https://leetcode.com/problems/dota2-senate/)                     | [go](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/Dota2Senate.go)     | 1 queue and [2 queues](https://leetcode.com/problems/dota2-senate/solutions/3483399/simple-diagram-explanation/?source=submission-ac) |

# cracking the coding interview questions

### Chapter 3: Stacks and Queues

| problem              | leetcode problem                                                                                    | code                                                                                                     | solution | my notes |
| -------------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------- | -------- |
| 3.1 Three In One     |                                                                                                     |                                                                                                          |
| 3.2 Stack Min        | 🟡 [155. Min Stack](https://leetcode.com/problems/min-stack/)                                       | [php](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/medium/MinStack.php)                  |
| 3.3 Stack of Plates  | 🔴 [1172. Dinner Plate Stacks](https://leetcode.com/problems/dinner-plate-stacks/)                  | [python](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/unsolved/DinnerPlateStacks.py)     |
| 3.4 Queue via Stacks | 🟢 [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | [python](https://github.com/shayansm2/leetcodeSolutions/blob/main/src/easy/ImplementQueueUsingStacks.py) |
| 3.5 Sort Stacks      |                                                                                                     |                                                                                                          |
| 3.6 Animal Shelter   |                                                                                                     |                                                                                                          |

---

### notes:

#### Monotonic Stack

A monotonic stack is a stack whose elements are monotonically increasing or decreasing.
Sometimes we store the index of the elements in the stack and make sure the elements corresponding to those indexes in
the stack forms a mono-sequence. **the usage of this stack is to when we want to know to next max/min element of each
element in an array.** it also can be used to get the minimum upward line or maximum downward line in a trend.

![img.png](MonotonicStack.png)

there are two ways you can implement the monotonic queue

```go
package main

func ForwardTraverse(nums []int) {
	var stack []int // ascending
	for _, val := range nums {
		for len(stack) > 0 && stack[len(stack)-1] < val {
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, val)
	}
}

```

```go
package main

func BackwardTraverse(nums []int) {
	var stack []int // descending
	for i := len(nums) - 1; i >= 0; i-- {
		val := nums[i]

		if len(stack) > 0 && stack[len(stack)-1] < val {
			stack = append(stack, val)
		}
	}
}
```

source for other [problems of monotonic stack](https://leetcode.com/tag/monotonic-stack/)

#### Car Fleet Solution

```go
package main

import "sort"

type Car struct {
	initPosition int
	speed        int
}

func carFleet(target int, position []int, speed []int) int {
	cars := make([]Car, len(position))
	for i := range position {
		cars[i] = Car{initPosition: position[i], speed: speed[i]}
	}

	sort.Slice(cars, func(i, j int) bool {
		return cars[i].initPosition < cars[j].initPosition
	})

	arrivalTimeStack := []float32{}

	// BackwardTraverse
	for i := len(cars) - 1; i >= 0; i-- {
		arrivalTime := float32(target-cars[i].initPosition) / float32(cars[i].speed)
		if len(arrivalTimeStack) == 0 || arrivalTimeStack[len(arrivalTimeStack)-1] < arrivalTime {
			arrivalTimeStack = append(arrivalTimeStack, arrivalTime)
		}
	}

	// ForwardTraverse
	for _, car := range cars {
		arrivalTime := float32(target-car.initPosition) / float32(car.speed)
		for len(arrivalTimeStack) > 0 && arrivalTimeStack[len(arrivalTimeStack)-1] <= arrivalTime {
			arrivalTimeStack = arrivalTimeStack[:len(arrivalTimeStack)-1]
		}
		arrivalTimeStack = append(arrivalTimeStack, arrivalTime)
	}

	return len(arrivalTimeStack)
}

```
