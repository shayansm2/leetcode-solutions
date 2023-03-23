class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if n - 1 > len(connections):
            return -1

        nodes = [[] for i in range(n)]
        visited = [False for i in range(n)]

        for a, b in connections:
            nodes[a].append(b)
            nodes[b].append(a)

        number_of_networks = 0

        for node_id, node in enumerate(nodes):
            if visited[node_id]:
                continue

            number_of_networks += 1
            queue = [node_id]

            while queue:
                cur_node_id = queue.pop()
                node = nodes[cur_node_id]
                visited[cur_node_id] = True

                for neighbour in node:
                    if visited[neighbour]:
                        continue
                    queue.append(neighbour)

        return number_of_networks - 1
