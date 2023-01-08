class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        length = len(points)

        if length == 1:
            return 1

        lines = dict()

        for i in range(length-1):
            for j in range(i+1, length):
                [x1, y1] = points[i]
                [x2, y2] = points[j]

                a, b = self.get_line(x1, x2, y1, y2)

                print([x1, y1], [x2, y2], (a, b))

                if (a, b) in lines.keys():
                    lines[(a, b)] += 1
                else:
                    lines[(a, b)] = 1

        pair_points = max(lines.values())

        return int((1 + ((1+8*pair_points)**(1/2)))/2)

    def get_line(self, x1, x2, y1, y2):
        if x2 == x1:
            a = float('inf')
            b = x1
        else:
            a = (y2 - y1) / (x2 - x1)
            b = y1 - a * x1

        return round(a, 4), round(b, 4)