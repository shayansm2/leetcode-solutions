class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        neighbours = [[] for i in range(n)]
        visited = [False for i in range(n)]

        for edge in edges:
            a, b = edge
            neighbours[a].append(b)
            neighbours[b].append(a)

        queue = [source]

        while queue:
            node = queue.pop()

            if node == destination:
                return True

            if visited[node]:
                continue

            visited[node] = True

            for neighbour in neighbours[node]:
                if visited[neighbour]:
                    continue

                queue.append(neighbour)
        return False
