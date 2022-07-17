class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = dict()
        
        for letter in s:
            try:
                counter[letter] += 1
            except:
                counter[letter] = 1

        has_odd_number = False
        longest_palindrome_length = 0

        for letter in counter.keys():
            longest_palindrome_length += (counter[letter] // 2) * 2
            
            if counter[letter] % 2 == 1:
                has_odd_number = True

        if has_odd_number:
            longest_palindrome_length += 1

        return longest_palindrome_length