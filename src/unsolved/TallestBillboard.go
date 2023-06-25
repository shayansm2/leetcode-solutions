package unsolved

import (
	"sort"
)

func tallestBillboard(rods []int) int {
	sort.Ints(rods)
	return BillboardBuilder{rods}.build()
}

type BillboardBuilder struct {
	rods []int
}

func (this BillboardBuilder) build() int {
	arraySum := 0
	for _, rod := range this.rods {
		arraySum += rod
	}
	this.idk(len(this.rods)-1, len(this.rods), arraySum, 0)
	return 1
}

func (this BillboardBuilder) idk(migrateEndIndex int, removeStartIndex int, sum1 int, sum2 int) {
	diff := (sum1 - sum2) / 2
	endIndex := this.findLastIndexLessThanOrEqualTo(diff)
	startIndex := this.findFirstIndexGreaterThanOrEqualTo(diff - this.rods[migrateEndIndex])
	for i := startIndex; i <= endIndex; i++ {
		this.idk(i-1, i+1, sum1-this.rods[i], sum2+this.rods[i])
	}
}

func (this BillboardBuilder) findLastIndexLessThanOrEqualTo(number int) int {
	return 1
}

func (this BillboardBuilder) findFirstIndexGreaterThanOrEqualTo(number int) int {
	return 1
}
