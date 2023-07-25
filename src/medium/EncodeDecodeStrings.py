class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def __init__(self):
        self.__char_len = 3
        self.__delimiter = '--'

    def encode(self, strs):
        return self.__delimiter.join(list(map(lambda x: self._encode_string(x), strs)))

    def _encode_string(self, string: str) -> str:
        return ''.join(list(map(lambda x: self._encode_char(x), list(string))))

    def _encode_char(self, char: str) -> str:
        result = str(ord(char))
        return result if len(result) >= self.__char_len else '0' * (self.__char_len - len(result)) + result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        return list(map(lambda x: self._decode_string(x), str.split(self.__delimiter)))

    def _decode_string(self, string: str) -> str:
        chars = [string[i:i + self.__char_len] for i in range(0, len(string), self.__char_len)]
        return ''.join(list(map(lambda x: self.__decode_char(x), chars)))

    def __decode_char(self, order: str) -> str:
        return chr(int(order))


sol = Solution()
res = sol.encode(['hello', 'shayan', 'how are you', 'can you encode this?'])
print(res)
print(sol.decode(res))
