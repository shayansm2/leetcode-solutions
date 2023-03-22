class TreeNode(object):
    def __init__(self, character: str):
        self.character = character
        self.neighbours = set()

    def add_neighbour(self, node_id: int):
        self.neighbours.add(node_id)

    def remove_neighbour(self, node_id: int):
        self.neighbours.remove(node_id)

    def __repr__(self):
        return self.character


class Solution:
    def __init__(self):
        self.trees = None
        self.nodes = None

    def longestPath(self, parent: list[int], s: str) -> int:
        self.init_tree(s, parent)
        max_length = 0
        for tree in self.trees:
            max_length = max(max_length, self.get_length(tree))
        return max_length

    def init_tree(self, s, parents):
        nodes = dict()
        trees = [0]

        for index, char in enumerate(s.strip()):
            nodes[index] = TreeNode(char)

        for child_id, parent_id in enumerate(parents):
            if parent_id == -1:
                continue

            child: TreeNode = nodes[child_id]
            parent: TreeNode = nodes[parent_id]

            if child.character == parent.character:
                trees.append(child_id)
            else:
                child.add_neighbour(parent_id)
                parent.add_neighbour(child_id)

        self.nodes = nodes
        self.trees = trees

    def get_length(self, tree: int) -> int:
        length = 0
        visited = {tree: tree}
        queue = [tree]

        while queue:
            current_node_id = queue.pop()
            current_node: TreeNode = self.nodes[current_node_id]
            length += 1

            for neighbour_id in current_node.neighbours:
                if not neighbour_id in visited.keys():
                    visited[neighbour_id] = neighbour_id
                    queue.append(neighbour_id)

        return length


test_cases = [
    {
        'input': {
            'parent': [-1, 0, 0, 1, 1, 2],
            's': 'abacbe',
        },
        'output': 3
    },
    {
        'input': {
            'parent': [-1, 0, 0, 0],
            's': 'aabc',
        },
        'output': 3
    },
    {
        'input': {
            'parent': [-1, 137, 65, 60, 73, 138, 81, 17, 45, 163, 145, 99, 29, 162, 19, 20, 132, 132, 13, 60, 21, 18,
                       155, 65, 13, 163, 125, 102, 96, 60, 50, 101, 100, 86, 162, 42, 162, 94, 21, 56, 45, 56, 13, 23,
                       101, 76, 57, 89, 4, 161, 16, 139, 29, 60, 44, 127, 19, 68, 71, 55, 13, 36, 148, 129, 75, 41, 107,
                       91, 52, 42, 93, 85, 125, 89, 132, 13, 141, 21, 152, 21, 79, 160, 130, 103, 46, 65, 71, 33, 129,
                       0, 19, 148, 65, 125, 41, 38, 104, 115, 130, 164, 138, 108, 65, 31, 13, 60, 29, 116, 26, 58, 118,
                       10, 138, 14, 28, 91, 60, 47, 2, 149, 99, 28, 154, 71, 96, 60, 106, 79, 129, 83, 42, 102, 34, 41,
                       55, 31, 154, 26, 34, 127, 42, 133, 113, 125, 113, 13, 54, 132, 13, 56, 13, 42, 102, 135, 130, 75,
                       25, 80, 159, 39, 29, 41, 89, 85, 19],
            's': 'ajunvefrdrpgxltugqqrwisyfwwtldxjgaxsbbkhvuqeoigqssefoyngykgtthpzvsxgxrqedntvsjcpdnupvqtroxmbpsdwoswxfarnixkvcimzgvrevxnxtkkovwxcjmtgqrrsqyshxbfxptuvqrytctujnzzydhpal',
        },
        'output': 3
    }
]

for test_case in test_cases:
    answer = Solution().longestPath(
        test_case['input']['parent'],
        test_case['input']['s']
    )
    if test_case['output'] != answer:
        print(answer, test_case)
