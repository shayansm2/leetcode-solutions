class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        is_vowel = [char in "aeiou" for char in s]
        cumsum = []
        summation = 0
        for i in is_vowel:
            summation += i
            cumsum.append(summation)

        max_vowels = cumsum[k - 1]

        for i in range(k, len(cumsum)):
            # print(i, i-k-1)
            max_vowels = max(max_vowels, cumsum[i] - cumsum[i - k])

        # print(is_vowel, cumsum)
        return max_vowels
