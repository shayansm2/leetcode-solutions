class Solution:
    def findShortestCycle(self, n: int, edges: list[list[int]]) -> int:
        nodes = [[] for i in range(n)]

        for edge in edges:
            a, b = edge
            nodes[a].append(b)
            nodes[b].append(a)

        visit_sequence = [None for i in range(n)]
        cycles = []

        for i in range(len(visit_sequence)):
            if visit_sequence[i] is not None:
                continue

            queue = [i]
            visit_sequence[i] = str(i)

            while queue:
                node_id = queue.pop(0)  # BFS
                # print('node', node_id, visit_sequence[node_id])

                for neighbour_id in nodes[node_id]:
                    if visit_sequence[neighbour_id] is None:
                        queue.append(neighbour_id)
                        visit_sequence[neighbour_id] = visit_sequence[node_id] + str(neighbour_id)
                    else:
                        # print(node_id, visit_sequence[node_id])
                        if visit_sequence[neighbour_id] + str(node_id) == visit_sequence[node_id]:
                            continue

                        # print(neighbour_id, visit_sequence[neighbour_id])

                        for j in range(min(len(visit_sequence[neighbour_id]), len(visit_sequence[node_id]))):
                            if visit_sequence[neighbour_id][j] != visit_sequence[neighbour_id][j]:
                                break

                        print('cycle', j, node_id, neighbour_id, visit_sequence[node_id], visit_sequence[neighbour_id],
                              len(visit_sequence[node_id]) + len(visit_sequence[neighbour_id]) - 2*j + 1)
                        cycles.append(len(visit_sequence[node_id]) + len(visit_sequence[neighbour_id]) - 2*j + 1)

        if cycles:
            return min(cycles)

        return -1


samples = [
    # [7, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]], 3],
    # [4, [[0, 1], [0, 2]], -1],
    # [3, [[0, 1], [1, 2]], -1],
    [6, [[4, 1], [5, 1], [3, 2], [5, 0], [4, 0], [3, 0], [2, 1]], 4],
    # [4, [[1, 2], [0, 1], [3, 2], [1, 3]], 3]
]

for sample in samples:
    if sample[2] != (Solution()).findShortestCycle(sample[0], sample[1]):
        print(sample, (Solution()).findShortestCycle(sample[0], sample[1]))
