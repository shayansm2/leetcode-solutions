# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        cloned_nodes = dict()

        cloned_nodes[node.val] = Node(node.val)
        queue = [node]

        while queue:
            # 1. create new neighbours if not exists
            # 2. add the old neighbours to the queue for BFS
            # 3. set new_node.neighbors = new_neighbours
            current_node: Node = queue.pop(0)
            cloned_node: Node = cloned_nodes[current_node.val]

            new_neighbours = []
            for neighbor in current_node.neighbors:
                neighbor: Node

                if neighbor.val not in cloned_nodes:
                    cloned_nodes[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)

                new_neighbours.append(cloned_nodes[neighbor.val])

            cloned_node.neighbors = new_neighbours

        return cloned_nodes[node.val]
