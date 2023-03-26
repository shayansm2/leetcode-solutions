class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        longest_cycle = -1
        visited = [False for _ in range(len(edges))]
        for node in range(len(edges)):
            if visited[node]:
                continue

            queue = [node]
            turn = 0
            turns = {}

            while queue:
                turn += 1
                current_node = queue.pop(0)
                visited[current_node] = True

                turns[current_node] = turn

                next_node = edges[current_node]

                if next_node == -1:
                    continue

                if next_node in turns:
                    longest_cycle=max(longest_cycle, turn + 1 - turns[next_node])
                    continue

                queue.append(next_node)

        return longest_cycle
