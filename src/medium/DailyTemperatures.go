package main

type temperatureInfo struct {
	id          int
	temperature int
}

type temperatureInfoStack []temperatureInfo

func (stack *temperatureInfoStack) getLast() *temperatureInfo {
	if len(*stack) == 0 {
		return nil
	}
	return &(*stack)[len(*stack)-1]
}

func (stack *temperatureInfoStack) pop() *temperatureInfo {
	info := stack.getLast()
	*stack = (*stack)[:len(*stack)-1]
	return info
}

func (stack *temperatureInfoStack) push(info temperatureInfo) {
	*stack = append(*stack, info)
}

func dailyTemperatures(temperatures []int) []int {
	answer := make([]int, len(temperatures))
	var stack temperatureInfoStack

	for i, temperature := range temperatures {
		info := temperatureInfo{id: i, temperature: temperature}

		for stack.getLast() != nil && stack.getLast().temperature < info.temperature {
			oldInfo := stack.pop()
			answer[oldInfo.id] = info.id - oldInfo.id
		}

		stack.push(info)
	}

	return answer
}
