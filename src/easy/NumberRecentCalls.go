package main

type RecentCounter struct {
	q []int
}

func RecentCounterConstructor() RecentCounter {
	return RecentCounter{q: make([]int, 0)}
}

func (this *RecentCounter) Ping(t int) int {
	this.q = append(this.q, t)
	for t-this.q[0] <= 3000 {
		this.q = this.q[1:]
	}
	return len(this.q)
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */
