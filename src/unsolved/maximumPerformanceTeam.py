from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = []

        for i in range(n):
            engineers.append({
                'speed': speed[i],
                'efficiency': efficiency[i]
            })

        engineers.sort(key=lambda x: x['efficiency'], reverse=True)  # O(nlogn)

        selectedEngineers = engineers[:k]
        speeds = list(map(lambda x: x['speed'], selectedEngineers))
        speeds.sort()

        minSpeed = speeds[0]
        totalSpeed = sum(speeds)
        maximumPerformance = totalSpeed * selectedEngineers[-1]['efficiency']

        for i in range(k, n):  # O(n)
            newEngineer = engineers[i]
            if newEngineer['speed'] <= minSpeed:
                continue

            totalSpeed += (newEngineer['speed'] - minSpeed)
            speeds = self.sortAgain(speeds[1:], newEngineer['speed'])  # O(logn)
            minSpeed = speeds[0]
            maximumPerformance = max(maximumPerformance, totalSpeed * newEngineer['efficiency'])

        return maximumPerformance

    def sortAgain(self, speeds: List, new_speed: int) -> List:
        start = 0  # inclusive
        end = len(speeds)  # exclusive

        while start < end:
            mid = start + ((end - start) // 2)

            if speeds[mid] < new_speed:
                start = mid + 1
                continue

            if mid > start:
                end = mid
                continue

            break

        speeds.insert(start, new_speed)
        return speeds


print(Solution().maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=2))
print(Solution().maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=3))
print(Solution().maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4))
print(Solution().maxPerformance(3, [2, 8, 2], [2, 7, 1], 2))
