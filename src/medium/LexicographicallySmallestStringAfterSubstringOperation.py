class Solution:
    def smallestString(self, s: str) -> str:
        start_replacing = False
        string = list(s)

        for i, char in enumerate(s):
            if char == 'a':
                if start_replacing:
                    break
                else:
                    continue

            start_replacing = True
            string[i] = chr(ord(char) - 1)

        if not start_replacing:
            string[-1] = "z"

        return ''.join(string)
