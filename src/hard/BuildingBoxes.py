class Solution:
    def minimumBoxes(self, n: int) -> int:
        i = 1
        totalCubes = 1

        while totalCubes < n:
            i += 1
            totalCubes += ((i * (i + 1)) / 2)

        if totalCubes == n:
            return int(((i * (i + 1)) / 2))

        totalBoxes = totalCubes - ((i * (i + 1)) / 2)
        floorBoxes = ((i * (i - 1)) / 2)

        for j in range(1, i + 1):
            if totalBoxes >= n:
                return int(floorBoxes)

            totalBoxes += j
            floorBoxes += 1

        return int(floorBoxes)


print(Solution().minimumBoxes(10))
