package main

import (
	"container/heap"
	"fmt"
)

type FoodRatings struct {
	cuisine2Heap map[string]*foodHeap
	foodRates    map[string]int
	food2cuisine map[string]string
}

type Food struct {
	name   string
	rating int
}

type foodHeap []Food

func (h foodHeap) Len() int { return len(h) }

func (h foodHeap) Less(i, j int) bool {
	if h[i].rating == h[j].rating {
		return h[i].name < h[j].name
	}
	return h[i].rating > h[j].rating
}

func (h foodHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *foodHeap) Push(x interface{}) { *h = append(*h, x.(Food)) }

func (h *foodHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func Constructor(foods []string, cuisines []string, ratings []int) FoodRatings {
	this := FoodRatings{
		cuisine2Heap: make(map[string]*foodHeap),
		foodRates:    make(map[string]int),
		food2cuisine: make(map[string]string),
	}

	for i := 0; i < len(foods); i++ {
		cuisine := cuisines[i]
		foodItem := Food{
			name:   foods[i],
			rating: ratings[i],
		}

		this.foodRates[foodItem.name] = foodItem.rating
		this.food2cuisine[foodItem.name] = cuisine
		this.addToHeap(cuisine, foodItem)
	}

	return this
}

func (this *FoodRatings) addToHeap(cuisine string, foodItem Food) {
	if _, found := this.cuisine2Heap[cuisine]; !found {
		myHeap := make(foodHeap, 0)
		this.cuisine2Heap[cuisine] = &myHeap
		heap.Init(&myHeap)
	}

	heap.Push(this.cuisine2Heap[cuisine], foodItem)
}

func (this *FoodRatings) ChangeRating(food string, newRating int) {
	this.foodRates[food] = newRating
	foodItem := Food{
		name:   food,
		rating: newRating,
	}

	this.addToHeap(this.food2cuisine[food], foodItem)
}

func (this *FoodRatings) HighestRated(cuisine string) string {
	myHeap := this.cuisine2Heap[cuisine]
	for {
		foodItem := heap.Pop(myHeap).(Food)
		if foodItem.rating == this.foodRates[foodItem.name] {
			//fmt.Println(foodItem)
			heap.Push(myHeap, foodItem)
			return foodItem.name
		}
	}
}

func main() {
	obj := Constructor(
		[]string{"kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"},
		[]string{"korean", "japanese", "japanese", "greek", "japanese", "korean"},
		[]int{9, 12, 8, 15, 14, 7},
	)

	fmt.Println(obj.HighestRated("korean"))
	fmt.Println(obj.HighestRated("japanese"))
	obj.ChangeRating("sushi", 16)
	fmt.Println(obj.HighestRated("japanese"))
	obj.ChangeRating("ramen", 16)
	fmt.Println(obj.HighestRated("japanese"))
}
