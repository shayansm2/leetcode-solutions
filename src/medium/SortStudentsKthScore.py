class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        scores = []

        for i in range(len(score)):
            scores.append(score[i][k])

        sorted_indices = [i[0] for i in sorted(enumerate(scores), key=lambda x: x[1])][::-1]

        new_score = []

        for i in sorted_indices:
            new_score.append(score[i])

        return new_score
