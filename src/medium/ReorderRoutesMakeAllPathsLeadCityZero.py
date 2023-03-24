class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        nodes = [{'neighbours': [], 'not_accessed': [], 'visited': False} for i in range(n)]

        for connection in connections:
            a, b = connection
            nodes[a]['neighbours'].append(b)
            nodes[b]['not_accessed'].append(a)
            nodes[b]['neighbours'].append(a)

        counter = 0
        queue = [0]

        while queue:
            node_id = queue.pop(0)
            nodes[node_id]['visited'] = True

            for neighbour_id in nodes[node_id]['neighbours']:
                if nodes[neighbour_id]['visited']:
                    continue
                queue.append(neighbour_id)

                if node_id in nodes[neighbour_id]['not_accessed']:
                    counter += 1

        return counter
