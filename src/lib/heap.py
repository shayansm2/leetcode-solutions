import heapq

myHeap = [3, 1, 5]

# print(myHeap) >> [3, 1, 5]
heapq.heapify(myHeap)  # make a heap with elements of (myHeap = [3, 1, 5]) and store it in myHeap
# print(myHeap) >> [1, 3, 5]
heapq.heappush(myHeap, -5)  # add -5 to myHeap
# print(myHeap) [-5, 1, 5, 3]
minElement = heapq.heappop(myHeap)  # pop min element in myHeap and return value of min element

print(minElement)  # print -5
