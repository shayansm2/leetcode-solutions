class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        turn = time // (n - 1)
        remain = time % (n - 1)
        # print(turn, remain)
        return n - remain if turn % 2 else remain + 1
