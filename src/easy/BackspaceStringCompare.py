class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        text_s = self.get_actual_text(s)
        text_t = self.get_actual_text(t)
        return text_s == text_t

    @staticmethod
    def get_actual_text(s) -> str:
        text = []

        for char in s:
            if char == '#':
                if not text:
                    continue

                text.pop()
                continue

            text.append(char)

        return ''.join(text)


print(Solution().backspaceCompare(s="ab#c", t="ad#c"))
print(Solution().backspaceCompare(s="ab##", t="c#d#"))
print(Solution().backspaceCompare(s="a#c", t="b"))
print(Solution().backspaceCompare(s="##a#c", t="b"))
