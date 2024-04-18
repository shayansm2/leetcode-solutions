from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)

        visited = [False] * length

        visited[0] = True
        queue = [0]

        while queue:
            if visited[-1]:
                return True

            index = queue.pop()
            jump = nums[index]

            for i in range(1, jump + 1):
                if i + index >= length:
                    break

                if not visited[i + index]:
                    visited[i + index] = True
                    queue.append(i + index)

        return visited[-1]