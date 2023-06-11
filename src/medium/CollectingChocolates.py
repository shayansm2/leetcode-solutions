class Solution:
    def minCost(self, nums: list[int], x: int) -> int:
        min_vals_per_type = []
        for i in range(len(nums)):
            min_val = nums[i]
            min_vals = [min_val]
            for step in range(1, len(nums)):
                new_index = (i + step) % len(nums)
                min_val = min(min_val, nums[new_index])
                min_vals.append(min_val)
            min_vals_per_type.append(min_vals)

        result = None
        for max_steps in range(len(nums)):
            min_cost = 0
            for i in range(len(nums)):
                min_cost += min_vals_per_type[i][max_steps]
            min_cost += x * max_steps

            if result is None:
                result = min_cost

            if result < min_cost:
                break
            result = min_cost
        return result


print(Solution().minCost(nums=[20, 1, 15], x=5))
print(Solution().minCost(nums=[1, 2, 3], x=4))
print(Solution().minCost(nums=[31, 25, 18, 59], x=27))  # 119
print(Solution().minCost(nums=[15, 150, 56, 69, 214, 203], x=42))  # 298
