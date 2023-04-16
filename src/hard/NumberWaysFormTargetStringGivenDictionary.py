class Solution:
    def __init__(self):
        self.modulo = 1000000007

    def numWays(self, words: list[str], target: str) -> int:
        mapping = {}

        for word in words:
            for index, letter in enumerate(word):
                if index + 1 in mapping:
                    if letter in mapping[index + 1]:
                        mapping[index + 1][letter] += 1
                    else:
                        mapping[index + 1][letter] = 1
                else:
                    mapping[index + 1] = dict()
                    mapping[index + 1][letter] = 1

        dp = [[1 for i in range(len(words[0]))]]

        dp_row_length = len(words[0]) - len(target) + 1

        for t in range(1, len(target) + 1):
            dp_row = [0 for i in range(t)]
            for w in range(t, t + dp_row_length):
                if w in mapping and target[t - 1] in mapping[w]:
                    dp_row.append(((dp[t - 1][w - 1] * mapping[w][target[t - 1]]) % self.modulo + dp_row[
                        -1] % self.modulo) % self.modulo)
                else:
                    dp_row.append(dp_row[-1])

            dp.append(dp_row)

        # print(dp)
        return dp[-1][-1]


use_cases = [
    {'words': ["acca", "bbbb", "caca"], 'target': "aba", 'output': 6},
    {'words': ["abba", "baab"], 'target': "bab", 'output': 4}
]

for use_case in use_cases:
    print(Solution().numWays(use_case['words'], use_case['target']))
