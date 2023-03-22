from typing import List
import json


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:  # o(n^3)
        ports = []
        weights = []

        for box in boxes:  # o(n)
            ports.append(box[0])
            weights.append(box[1])

        f = [2]
        for boxIndex in range(1, len(boxes)):  # o(n)
            packageWeight = weights[boxIndex]
            packageLength = 1 + 1

            numberOfTripsForThisPackage = 2
            f_currentBox = numberOfTripsForThisPackage + f[boxIndex - 1]

            while packageLength <= maxBoxes:  # o(n)
                if packageLength > boxIndex + 1:
                    break

                packageStartIndex = boxIndex + 1 - packageLength

                packageWeight += weights[packageStartIndex]

                if packageWeight > maxWeight:
                    break

                # if packageStartIndex >= 1 and ports[packageStartIndex] == ports[packageStartIndex - 1] and packageLength + 1 <= maxBoxes and packageWeight + weights[packageStartIndex - 1] <= maxWeight:
                #     packageLength += 1
                #     packageWeight += weights[packageStartIndex - 1]
                #     continue

                if ports[packageStartIndex] != ports[packageStartIndex + 1]:
                    numberOfTripsForThisPackage += 1

                f_this = numberOfTripsForThisPackage
                if packageStartIndex >= 1:
                    f_this += f[packageStartIndex - 1]

                f_currentBox = min(f_currentBox, f_this)

                packageLength += 1

            f.append(f_currentBox)

        print(f)
        return f[-1]


print(Solution().boxDelivering(boxes=[[1, 1], [2, 1], [1, 1]], portsCount=2, maxBoxes=3, maxWeight=3))
print(Solution().boxDelivering([[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]], portsCount=3, maxBoxes=3, maxWeight=6))
print(Solution().boxDelivering(
    boxes=[[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]], portsCount=3, maxBoxes=6, maxWeight=7
))
# json_file = open('boxesTestCase.json')
# boxes = json.load(json_file)
# print(Solution().boxDelivering(boxes=boxes, portsCount=100000, maxBoxes=60000, maxWeight=100000))
