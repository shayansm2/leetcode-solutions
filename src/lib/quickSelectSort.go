package lib

type IntList []int

func (list IntList) swap(index1, index2 int) { list[index1], list[index2] = list[index2], list[index1] }

func QuickSelect(list []int, k int) int {
	intList := getIntList(list)
	return quickSelect(intList, 0, len(intList)-1, k)
}

func QuickSort(list []int) {
	intList := getIntList(list)
	quickSort(intList, 0, len(intList)-1)
}

func getIntList(list []int) IntList {
	intList := make(IntList, len(list))
	for i, v := range list {
		intList[i] = v
	}
	return intList
}

func quickSort(list IntList, start int, end int) {
	if start == end {
		return
	}

	pivotIndex := start + ((end - start) / 2)
	pivotIndex = partition(list, start, end, pivotIndex)
	quickSort(list, start, pivotIndex-1)
	quickSort(list, pivotIndex+1, end)
}

func quickSelect(list IntList, left int, right int, k int) int {
	if left == right {
		return list[left]
	}

	pivotIndex := left + ((right - left) / 2)
	pivotIndex = partition(list, left, right, pivotIndex)

	if k == pivotIndex {
		return list[k]
	} else if k < pivotIndex {
		return quickSelect(list, left, pivotIndex-1, k)
	} else {
		return quickSelect(list, pivotIndex+1, right, k)
	}
}

func partition(list IntList, left int, right int, pivotIndex int) int {
	pivotValue := list[pivotIndex]
	list.swap(pivotIndex, right)
	storeIndex := left

	for i := left; i < right; i++ {
		if list[i] < pivotValue {
			list.swap(storeIndex, i)
			storeIndex++
		}
	}

	list.swap(right, storeIndex)
	return storeIndex
}
