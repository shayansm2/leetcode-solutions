class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            if char == "B" and len(stack) > 0 and stack[-1] == "A":
                stack.pop()
            elif char == "D" and len(stack) > 0 and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(char)

        return len(stack)
