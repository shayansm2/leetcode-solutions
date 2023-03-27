class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        longest_cycle = -1
        visited = [False for _ in range(len(edges))]

        for node in range(len(edges)):
            if visited[node]:
                print('badi')
                continue

            print('new graph starting with', node)

            next_node = node
            turn = 0
            turns = dict()

            while next_node is not None:
                turn += 1
                current_node, next_node = next_node, None

                print(sum(visited), current_node, turn)

                visited[current_node] = True

                turns[current_node] = turn

                next_node = edges[current_node]

                if next_node == -1:
                    break

                if next_node in turns:
                    longest_cycle = max(longest_cycle, turn + 1 - turns[next_node])
                    break

                if visited[next_node]:
                    break

        return longest_cycle


if __name__ == '__main__':
    in1 = [3, 3, 4, 2, 3]
    in2 = [2, -1, 3, 1]
    in3 = [3, 4, 0, 2, -1, 2]
    in4 = [-1, 4, -1, 2, 0, 4]
    in5 = list(map(int, input()[1:-1].split(',')))
    in6 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1, 1, 2, 3]
    print(Solution().longestCycle(in5))
