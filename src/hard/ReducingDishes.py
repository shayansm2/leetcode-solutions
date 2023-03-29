class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction = sorted(satisfaction)
        positive_sum = 0
        negative_sum = 0
        breaking_index = -1
        for i in range(len(satisfaction) - 1, -1, -1):
            num = satisfaction[i]

            if num > 0:
                positive_sum += num
            else:
                negative_sum -= num
                if negative_sum >= positive_sum:
                    breaking_index = i
                    break

        like_time_coefficient = 0
        for i in range(breaking_index + 1, len(satisfaction)):
            like_time_coefficient += ((i - breaking_index) * satisfaction[i])

        return like_time_coefficient
