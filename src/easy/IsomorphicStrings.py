class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = {}
        reverse_mapper = {}

        if len(s) != len(t):
            return False

        length = len(s)

        for index in range(length):
            if mapper.__contains__(s[index]):
                if mapper[s[index]] != t[index]:
                    return False
            else:
                if reverse_mapper.__contains__(t[index]):
                    return False

                mapper[s[index]] = t[index]
                reverse_mapper[t[index]] = s[index]

        return True
