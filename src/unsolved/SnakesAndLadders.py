import time


class Node:
    def __init__(self, node_id: int):
        self.id = node_id
        self.neighbours = set()
        self.distance = -1
        self.is_ladder_or_snake = False
        self.path = []

    def add_neighbour(self, neighbour_id: int):
        self.neighbours.add(neighbour_id)

    def set_distance(self, distance: int):
        self.distance = distance

    def set_path(self, path: list):
        self.path = path

    def set_is_ladder_or_snake(self):
        self.is_ladder_or_snake = True

    def __repr__(self):
        return '\n [' + str(self.id) + ' | N: ' + (','.join(list(map(str, list(self.neighbours))))) + ' | D:' + str(
            self.distance) + ' | P:' + ('-'.join(list(map(str, self.path)))) + ']'


class Solution:
    def __init__(self):
        self.nodes = dict()

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        self.create_graph(board)
        self.run_bfs()
        print(self.nodes.values())
        n = len(board)
        return self.nodes[n ** 2].distance

    def create_graph(self, board: list[list[int]]):
        n = len(board)

        for row_id, row in enumerate(board):
            for column_id, target_id in enumerate(row):
                house_id = n * (n - row_id)
                if (n - row_id) % 2 == 1:
                    house_id -= (n - column_id - 1)
                else:
                    house_id -= column_id

                node = Node(house_id)

                if board[row_id][column_id] == -1:
                    for neighbour_id in range(house_id + 1, min(house_id + 7, n ** 2 + 1)):
                        node.add_neighbour(neighbour_id)
                else:
                    node.add_neighbour(board[row_id][column_id])
                    node.set_is_ladder_or_snake()

                self.nodes[house_id] = node

    def run_bfs(self):
        visited = dict()

        for node_id in self.nodes.keys():
            visited[node_id] = False

        visited[1] = True
        first_node: Node = self.nodes[1]
        first_node.set_distance(0)
        first_node.set_path([1])
        queue = [first_node]

        while queue:
            # print(queue)
            # time.sleep(1)
            min_index = 0
            min_value = queue[0].distance
            # print('min_value', min_value)
            for i, node in enumerate(queue):
                # print('node.distance', node.distance)
                if node.distance < min_value:
                    min_index = i
                    min_value = node.distance

            # print(min_index)
            current_node: Node = queue.pop(min_index)
            # current_node: Node = queue.pop(0)
            current_distance = current_node.distance
            is_snake_or_ladder = current_node.is_ladder_or_snake

            for neighbour_id in current_node.neighbours:
                neighbour: Node = self.nodes[neighbour_id]
                if visited[neighbour_id]:
                    # print('current_node.distance', current_node.distance, 'neighbour.distance', neighbour.distance)
                    continue

                if is_snake_or_ladder:
                    neighbour.set_distance(current_distance)
                else:
                    neighbour.set_distance(current_distance + 1)

                neighbour.set_path(current_node.path + [neighbour.id])
                queue.append(neighbour)
                visited[neighbour_id] = True


case1 = [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]

case2 = [[-1, -1], [-1, 3]]

case3 = [[-1, -1, -1],
         [-1, 9, 8],
         [-1, 8, 9]]

case4 = [[-1, 1, 2, -1],
         [2, 13, 15, -1],
         [-1, 10, -1, -1],
         [-1, 6, 2, 8]]

print(Solution().snakesAndLadders(case4))
