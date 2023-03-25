class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        self.nodes = self.create_graph(n, edges)

        networks = []

        for node_id, node in enumerate(self.nodes):
            if node['visited']:
                continue

            networks.append(self.get_network_nodes_count(node_id))

        print(networks)
        result = 0

        for i in range(len(networks) - 1):
            n -= networks[i]
            result += (n * networks[i])

        return result

    def create_graph(self, n, edges):
        nodes = [{'neighbours': [], 'visited': False} for i in range(n)]

        for edge in edges:
            a, b = edge
            nodes[a]['neighbours'].append(b)
            nodes[b]['neighbours'].append(a)

        return nodes

    def get_network_nodes_count(self, start_node_id):
        network_nodes_count = 0

        queue = [start_node_id]

        while queue:
            node_id = queue.pop(0)

            if self.nodes[node_id]['visited']:
                continue

            network_nodes_count += 1
            self.nodes[node_id]['visited'] = True

            for neighbour_id in self.nodes[node_id]['neighbours']:
                if self.nodes[neighbour_id]['visited']:
                    continue

                queue.append(neighbour_id)

        return network_nodes_count
