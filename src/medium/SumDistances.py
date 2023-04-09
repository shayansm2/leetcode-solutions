class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        reverse_index = dict()
        prefix_sums = dict()

        for i, number in enumerate(nums):
            if number in reverse_index:
                reverse_index[number].append(i)
                prefix_sums[number].append(prefix_sums[number][-1] + i)
            else:
                reverse_index[number] = [i]
                prefix_sums[number] = [i]

        arr = []

        for i, number in enumerate(nums):
            indices = reverse_index[number]
            value = 0
            if len(indices) > 1:
                prefix_sum = prefix_sums[number]
                index = self.binary_search(indices, i)
                # print(prefix_sum, index)
                # print(prefix_sum[-1] - prefix_sum[index] , (len(prefix_sum) - index - 1) * i, (index+1) * i , prefix_sum[index])
                value = (prefix_sum[-1] - prefix_sum[index] - (len(prefix_sum) - index - 1) * i) + (
                        (index + 1) * i - prefix_sum[index])

            arr.append(value)

        return arr

    @staticmethod
    def binary_search(array, target):
        low = 0  # inclusive
        high = len(array) - 1  # inclusive

        # Repeat until the pointers low and high meet each other
        while low <= high:

            mid = low + (high - low) // 2

            if array[mid] == target:
                return mid

            if array[mid] < target:
                low = mid + 1
                continue

            high = mid - 1

        return -1
