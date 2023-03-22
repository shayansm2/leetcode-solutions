from typing import Optional


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['#'] = True

    def search(self, word: str) -> bool:
        node = self._search(word)
        return node is not None and '#' in node

    def startsWith(self, prefix: str) -> bool:
        return self._search(prefix) is not None

    def _search(self, word: str) -> Optional[dict]:
        curr = self.trie
        for char in word:
            if char not in curr:
                return None
            curr = curr[char]
        return curr
