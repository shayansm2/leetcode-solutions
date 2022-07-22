from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # visited = []
        rows = len(image)
        columns = len(image[0])

        queue = [(sr, sc)]

        searchColor = image[sr][sc]

        while queue:
            pixel = queue.pop(0)
            # visited.append(pixel)
            i, j = pixel
            image[i][j] = color

            if i > 0 and image[i - 1][j] == searchColor and image[i - 1][j] != color:
                queue.append((i - 1, j))

            if j > 0 and image[i][j - 1] == searchColor and image[i][j - 1] != color:
                queue.append((i, j - 1))

            if i < rows - 1 and image[i + 1][j] == searchColor and image[i + 1][j] != color:
                queue.append((i + 1, j))

            if j < columns - 1 and image[i][j + 1] == searchColor and image[i][j + 1] != color:
                queue.append((i, j + 1))

        return image