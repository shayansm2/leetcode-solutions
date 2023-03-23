class Solution:
    def __init__(self):
        self.visited = None
        self.nodes = None

    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if not self.is_number_of_connections_sufficient(n, len(connections)):
            return -1

        self.create_graph(connections, n)

        return self.get_number_of_networks() - 1

    def get_number_of_networks(self):
        number_of_networks = 0
        for node_id, node in enumerate(self.nodes):
            if self.visited[node_id]:
                continue

            number_of_networks += 1
            self.perform_DFS(node_id)
        return number_of_networks

    def perform_DFS(self, node_id):
        queue = [node_id]
        while queue:
            cur_node_id = queue.pop()
            node = self.nodes[cur_node_id]
            self.visited[cur_node_id] = True

            for neighbour in node:
                if self.visited[neighbour]:
                    continue
                queue.append(neighbour)

    def create_graph(self, connections, n):
        self.nodes = [[] for i in range(n)]
        self.visited = [False for i in range(n)]
        for a, b in connections:
            self.nodes[a].append(b)
            self.nodes[b].append(a)

    @staticmethod
    def is_number_of_connections_sufficient(number_of_nodes: int, number_of_connections: int) -> bool:
        return number_of_nodes - 1 <= number_of_connections
