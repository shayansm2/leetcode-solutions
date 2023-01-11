# problem 1:            find the min path from vertex 0 to collect all apples
# simplifier 1:         if we can get all the nodes which should be visited, we can calculate the path length by
#                       multiplying number of nodes with 2
# ----------------------------------------------------------------------------------------------------------------------
# problem 2:            find all the nodes which should be visited in order to collect all the apples
# simplifier 2:         if we travel from one apple node to another and append all the nodes in the middle we can get
#                       all the nodes in order to collect all the apples
# algorithm             visitedNodes = {}
#                       for fromNode in (vertex 0 + apple nodes):
#                           for toNode in (fromNode + 1 : rest of the nodes):
#                               nodesInBetween = min path from fromNode to toNode
#                               visitedNodes.append(nodesInBetween)
#                       return (count(visitedNodes) - 1) * 2
# ----------------------------------------------------------------------------------------------------------------------
# problem 3:            find the min path from 2 nodes
# solution 3:           there is only one path between two points which is the minimum path
#                       therefore the result of BFS and DFS is the same
# complexity analysis:  o(n^3)
# ----------------------------------------------------------------------------------------------------------------------
# problem 4:            cannot use this algo. the complexity should be o(n log n) not o(n^3)
# solution 4:           we traverse the whole tree form node 0 and stor the path from vertex 0 to each node
#                       then we get union of all visited nodes of apple nodes
# algorithm             run BFS and store path to each node
#                       visitedNodes = {}
#                       for appleNode in appleNodes:
#                           visitedNodes.append(appleNode.path)
#                       return count(visitedNodes) * 2
# complexity analysis:  o(n) or o(n log n) IDK!
# ----------------------------------------------------------------------------------------------------------------------
class Node(object):
    def __init__(self, node_id):
        self.id = node_id
        self.has_apple = False
        self.neighbour_ids = set()
        self.path = []

    def add_neighbour(self, neighbour_id: int):
        self.neighbour_ids.add(neighbour_id)

    def set_has_apple(self):
        self.has_apple = True

    def set_path(self, path: list):
        self.path = path

    def __repr__(self):
        id = 'id = ' + str(self.id)
        neighbours = 'neighbours = ' + ','.join(map(str, self.neighbour_ids))
        path = 'path = ' + ','.join(map(str, self.path))
        return path
        return id + '\n' + neighbours + '\n' + path


class Solution:
    def __init__(self):
        self.nodes = None

    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        self.init_nodes(edges, hasApple, n)
        self.run_bfs(n)
        visited_nodes = self.get_visited_nodes()

        if len(visited_nodes) == 0:
            return 0

        return (len(visited_nodes) - 1) * 2

    def init_nodes(self, edges, hasApple, n):
        nodes = dict()
        for i in range(n):
            nodes[i] = Node(i)
        for edge in edges:
            [from_node, to_node] = edge
            nodes[from_node].add_neighbour(to_node)
            nodes[to_node].add_neighbour(from_node)
        for node_id, has_apple in enumerate(hasApple):
            if has_apple:
                nodes[node_id].set_has_apple()

        self.nodes = nodes

    def run_bfs(self, n):
        visited = dict()
        for i in range(n):
            visited[i] = False

        queue = [0]
        self.nodes[0].set_path([0])

        while queue:
            current_node_id = queue.pop()
            current_node = self.nodes[current_node_id]
            current_path = current_node.path
            visited[current_node_id] = True

            for neighbour_id in current_node.neighbour_ids:
                if not visited[neighbour_id]:
                    queue.append(neighbour_id)
                    self.nodes[neighbour_id].set_path(current_path + [neighbour_id])

    def get_visited_nodes(self):
        visited = dict()

        for node in self.nodes.values():
            if node.has_apple:
                for visited_node in node.path:
                    visited[visited_node] = visited_node

        return visited.keys()


test_cases = [
    {
        'input': {
            'n': 7,
            'edges': [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            'hasApple': [False, False, True, False, True, True, False],
        },
        'output': 8
    },
    {
        'input': {
            'n': 7,
            'edges': [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            'hasApple': [False, False, True, False, False, True, False]
        },
        'output': 6
    },
    {
        'input': {
            'n': 7,
            'edges': [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            'hasApple': [False, False, False, False, False, False, False]
        },
        'output': 0
    }
]

for test_case in test_cases:
    if test_case['output'] != Solution().minTime(
            test_case['input']['n'],
            test_case['input']['edges'],
            test_case['input']['hasApple']
    ):
        print(test_case)
