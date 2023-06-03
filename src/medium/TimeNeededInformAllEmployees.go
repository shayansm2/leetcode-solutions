package main

type Employee struct {
	id           int
	employees    []int
	informedTime int
}

func (this *Employee) addEmployee(id int) {
	this.employees = append(this.employees, id)
}

func numOfMinutes(n int, headID int, manager []int, informTime []int) int {
	employees := make([]Employee, n)
	for i := 0; i < n; i++ {
		employees[i] = Employee{id: i}
	}
	for id, managerId := range manager {
		if managerId == -1 {
			continue
		}
		employees[managerId].addEmployee(id)
	}

	var maxInformedTime int
	employees[headID].informedTime = 0
	queue := []int{headID}
	for len(queue) > 0 {
		curManager := queue[0]
		queue = queue[1:]
		for _, emp := range employees[curManager].employees {
			employees[emp].informedTime = employees[curManager].informedTime + informTime[curManager]
			queue = append(queue, emp)
			if maxInformedTime < employees[emp].informedTime {
				maxInformedTime = employees[emp].informedTime
			}
		}
	}
	return maxInformedTime
}
