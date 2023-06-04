class PathStat(object):
    def __init__(self, unmodified_path_sum: int, modified_path_count: int = 0, edges: list[list] = []):
        self.unmodified_path_sum = unmodified_path_sum
        self.modified_path_count = modified_path_count
        self.edges = edges

    def __repr__(self):
        return 'distance: ' + str(self.unmodified_path_sum) + ' with ' + str(self.modified_path_count) + ' edges of -1'


class Solution:
    def modifiedGraphEdges(
            self,
            n: int,
            edges: list[list[int]],
            source: int,
            destination: int,
            target: int
    ) -> list[list[int]]:
        nodes = self.get_nodes_from_representation(n, edges)

        queue = [source]
        visited = [False for i in range(n)]
        path_stats = [PathStat(0)]
        final_path_stats = []

        while queue:
            node = queue.pop(0)
            path_stat = path_stats.pop(0)

            if visited[node]:
                continue

            visited[node] = True

            if node == destination:
                final_path_stats.append(path_stat)
                continue

            for neighbour, distance in nodes[node].items():
                queue.append(neighbour)
                if distance == -1:
                    path_stats.append(PathStat(
                        path_stat.unmodified_path_sum,
                        path_stat.modified_path_count + 1,
                        path_stat.edges + [node, neighbour]
                    ))
                else:
                    path_stats.append(PathStat(
                        path_stat.unmodified_path_sum + distance,
                        path_stat.modified_path_count,
                        path_stat.edges
                    ))

        print(final_path_stats)

        return self.get_representation_from_nodes(nodes)

    def get_nodes_from_representation(self, n: int, edges: list[list[int]]) -> list[dict]:
        nodes = [dict() for i in range(n)]
        for edge in edges:
            a, b, d = edge
            nodes[a][b] = d
            nodes[b][a] = d
        return nodes

    def get_representation_from_nodes(self, nodes: list[dict]) -> list[list[int]]:
        result = []
        nodes = nodes.copy()
        for a, node in enumerate(nodes):
            for b, d in node.items():
                del (nodes[b][a])
                result.append([a, b, d])
        return result


test_cases = [
    {'n': 5, 'edges': [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]], 'source': 0, 'destination': 1, 'target': 5},
    {'n': 3, 'edges': [[0, 1, -1], [0, 2, 5]], 'source': 0, 'destination': 2, 'target': 6},
    {'n': 4, 'edges': [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]], 'source': 0, 'destination': 2, 'target': 6}
]

for test_case in test_cases:
    Solution().modifiedGraphEdges(
        test_case['n'],
        test_case['edges'],
        test_case['source'],
        test_case['destination'],
        test_case['target']
    )
