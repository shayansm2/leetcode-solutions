# do I really need to create a whole network before traversing it? can't I traverse the network while building it?

class Node(object):
    def __init__(self, id: int, value: int):
        self.id = id
        self.value = value
        self.neighbour_ids = set()

    def add_neighbour_id(self, id: int):
        self.neighbour_ids.add(id)

    def get_neighbour_ids(self):
        return list(self.neighbour_ids)

    def __repr__(self):
        return 'id: ' + str(self.id) + ' value: ' + str(self.value) + ' neighbours: ' + '-'.join(
            map(str, self.get_neighbour_ids()))


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        nodes = self.create_nodes(arr)
        print(nodes.values())
        return self.bfs(nodes)

    def create_nodes(self, arr):
        nodes = dict()
        reverse_index = dict()
        for index, num in enumerate(arr):
            node = Node(index, num)

            if index > 0:
                node.add_neighbour_id(index - 1)
            if index < len(arr) - 1:
                node.add_neighbour_id(index + 1)

            nodes[index] = node

            if num in reverse_index.keys():
                reverse_index[num].append(index)
            else:
                reverse_index[num] = [index]
        for i in reverse_index.keys():
            if len(reverse_index[i]) <= 1:
                continue

            neighbours = reverse_index[i]
            for node_id in neighbours:
                for neighbour_id in neighbours:
                    if node_id == neighbour_id:
                        continue

                    nodes[node_id].add_neighbour_id(neighbour_id)
        return nodes

    def bfs(self, nodes: dict):
        src = 0
        des = len(nodes) - 1
        visited = dict()

        for i in nodes.keys():
            visited[i] = False

        queue = [src]
        distances = [0]

        while queue:
            node_id = queue.pop(0)
            node: Node = nodes[node_id]
            distance = distances.pop(0)

            visited[node_id] = True

            if node.id == des:
                return distance

            for neighbour_id in node.get_neighbour_ids():
                if visited[neighbour_id]:
                    continue

                queue.append(neighbour_id)
                distances.append(distance + 1)


Solution().minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404])
