from queue import Queue, PriorityQueue


def bfs(graph, start, end):
    """
    Compute DFS(Depth First Search) for a graph
    :param graph: The given graph
    :param start: Node to start BFS
    :param end: Goal-node
    """
    frontier = Queue()
    frontier.put(start)
    explored = []

    while True:
        if frontier.empty():
            raise Exception("No way Exception")
        current_node = frontier.get()
        explored.append(current_node)

        # Check if node is goal-node
        if current_node == end:
            return

        for node in graph[current_node]:
            if node not in explored:
                frontier.put(node)


def dfs(graph, start, end):
    """
    Compute dfs for a graph
    :param graph: The given graph
    :param start: Node to start bfs
    :param end: Goal-node
    """
    frontier = [start, ]
    explored = []

    while True:
        if len(frontier) == 0:
            raise Exception("No way Exception")
        current_node = frontier.pop()
        explored.append(current_node)

        # Check if node is goal-node
        if current_node == end:
            return

        # expanding nodes
        for node in reversed(graph[current_node]):
            if node not in explored:
                frontier.append(node)


def ucs_weight(from_node, to_node, weights=None):
    """
    Returns the UCS weight for a edge between from and to
    Assumption: There is no edge with weight >= 10e100 (You can change it)
    :param from_node: The node edge starts from
    :param to_node: The node edge ends to
    :param weights: Dictionary of weights; maps `(from, to) -> weight`
    :return: Returns the weight of edge between from and to.
    """
    return weights.get((from_node, to_node), 10e100) if weights else 1


def ucs(graph, start, end, weights=None):
    """
    Function to compute UCS(Uniform Cost Search) for a graph
    :param graph: The graph to compute UCS for
    :param start: start node
    :param end: end node
    :param weights: A dictionary of weights; maps (start_node, end_node) -> weight
    """
    frontier = PriorityQueue()
    frontier.put((0, start))  # (priority, node)
    explored = []

    while True:
        if frontier.empty():
            raise Exception("No way Exception")

        ucs_w, current_node = frontier.get()
        explored.append(current_node)

        if current_node == end:
            return

        for node in graph[current_node]:
            if node not in explored:
                frontier.put((
                    ucs_w + ucs_weight(current_node, node, weights),
                    node
                ))


if __name__ == "__main__":
    # This is Tree
    first_graph = {
        'A': ['B', 'C', 'D', 'E'],
        'B': ['A', 'F', 'G'],
        'C': ['A', 'H'],
        'D': ['A', 'I', 'J'],
        'E': ['A', 'K', 'L'],
        'F': ['B', 'M', 'N', 'O'],
        'G': ['B', 'P', 'Q', 'R'],
        'H': ['C', 'S'],
        'I': ['D'],
        'J': ['D', 'T', 'U'],
        'K': ['E'],
        'L': ['E', 'V'],
        'M': ['F'],
        'N': ['F'],
        'O': ['F'],
        'P': ['G'],
        'Q': ['G'],
        'R': ['G'],
        'S': ['H', 'W', 'X'],
        'T': ['J'],
        'U': ['J', 'Y', 'Z'],
        'V': ['L'],
        'W': ['S'],
        'X': ['S'],
        'Y': ['U'],
        'Z': ['U']
    }

    bfs(first_graph, 'A', 'Y')
    dfs(first_graph, 'A', 'Y')
    ucs(first_graph, 'A', 'Y')

    ucs_test_graph = {
        'S': ['A', 'B', 'C'],
        'A': ['S', 'G'],
        'B': ['S', 'G'],
        'C': ['S', 'G'],
        'G': ['A', 'B', 'C']
    }

    ucs_test_weight = {
        ('S', 'A'): 1,
        ('S', 'B'): 5,
        ('S', 'C'): 15,

        ('A', 'G'): 10,
        ('A', 'S'): 1,

        ('B', 'S'): 5,
        ('B', 'G'): 5,

        ('C', 'S'): 15,
        ('C', 'G'): 5,

        ('G', 'A'): 10,
        ('G', 'B'): 5,
        ('G', 'C'): 5,
    }

    ucs(ucs_test_graph, 'S', 'G', ucs_test_weight)

    # This is not Tree
    second_graph = {
        'A': ['B', 'C', 'D', 'E'],
        'B': ['A', 'F', 'G', 'H'],
        'C': ['A', 'H'],
        'D': ['A', 'I', 'J'],
        'E': ['A', 'K', 'L'],
        'F': ['B', 'G', 'M', 'N', 'O'],
        'G': ['B', 'F', 'P', 'Q', 'R'],
        'H': ['C', 'G', 'S'],
        'I': ['D'],
        'J': ['D', 'T', 'U'],
        'K': ['E'],
        'L': ['E', 'V'],
        'M': ['F'],
        'N': ['F'],
        'O': ['F'],
        'P': ['G'],
        'Q': ['G'],
        'R': ['G'],
        'S': ['H', 'W', 'X'],
        'T': ['J'],
        'U': ['J', 'Y', 'Z'],
        'V': ['L'],
        'W': ['S'],
        'X': ['S'],
        'Y': ['U'],
        'Z': ['U']
    }
    bfs(second_graph, 'A', 'Y')
    dfs(second_graph, 'A', 'Y')
    ucs(second_graph, 'A', 'Y')