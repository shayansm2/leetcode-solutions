class Solution:
    def getSubarrayBeauty(self, nums: list[int], k: int, x: int) -> list[int]:
        # print("original array", nums)
        ds = DataStructure()

        for i in range(k):
            if nums[i] < 0:
                # print("adding", nums[i])
                ds.add(nums[i])

        result = [ds.get_min_number(x)]

        for i in range(k, len(nums)):
            if nums[i - k] < 0:
                ds.remove(nums[i - k])
                # print("removing", nums[i - k])
            if nums[i] < 0:
                ds.add(nums[i])
                # print("adding", nums[i])
            result.append(ds.get_min_number(x))

        return result


class DataStructure():
    def __init__(self):
        self.array = []

    def add(self, element: int) -> None:
        if len(self.array) == 0:
            self.array.append(element)
            return
        index = self._iterative_binary_search(element, True)
        # print("insert index:", index, self.array, element)
        self.array.insert(index, element) if self.array[index] > element else self.array.insert(index + 1, element)

    def remove(self, element: int) -> None:
        index = self._iterative_binary_search(element)
        # print("pop index:", index, self.array, element)
        self.array.pop(index)

    def get_min_number(self, position: int) -> int:
        # print("state: ", self.array)
        if len(self.array) < position:
            return 0
        return self.array[position - 1]

    def _iterative_binary_search(self, target, find_nearest=False):
        low = 0  # inclusive
        high = len(self.array) - 1  # inclusive

        # Repeat until the pointers low and high meet each other
        while low <= high:

            mid = low + (high - low) // 2

            if self.array[mid] == target:
                return mid

            if self.array[mid] < target:
                low = mid + 1
                continue

            high = mid - 1

        if find_nearest:
            return mid
        return -1


samples = [
    {"nums": [1, -1, -3, -2, 3], "k": 3, "x": 2, "Output": [-1, -2, -2]},
    {"nums": [-1, -2, -3, -4, -5], "k": 2, "x": 2, "Output": [-1, -2, -3, -4]},
    {"nums": [-3, 1, 2, -3, 0, -3], "k": 2, "x": 1, "Output": [-3, 0, -3, -3, -3]},
    {"nums": [-48, -26], "k": 2, "x": 1, "Output": []},
]

for sample in samples:
    print(Solution().getSubarrayBeauty(sample["nums"], sample["k"], sample["x"]), sample["Output"])
