# n is the number of words
# l is the length of word

# | data structure                                    | add complexity | search complexity                  | result                              |
# |---------------------------------------------------|----------------|------------------------------------|-------------------------------------|
# | array                                             | O(1)           | O(n*l)                             ||
# | hash map                                          | O(1)           | O(1) normal word, O(n*l) wild card ||
# | trie tree                                         | O(l)           | O(l) normal word, O(n*l) wild card | True answer with combination of DFS |
# | trie tree for each world combination              | O(l * l!)      | O(l)                               ||
# | hash map letter + position                        | O(l)           | O(l*n)                             | good for startWith, not for search  |
# | hash map with generating all possible search word | O(1)           | O(26**3) ~= 10**5                  | time out                            |


class WordDictionary:

    def __init__(self):
        self.trie = dict()

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = dict()
            node = node[char]

        node['#'] = True

    def search(self, word: str) -> bool:
        queue = [self.trie]
        depths = [0]

        while queue:
            node = queue.pop()
            depth = depths.pop()

            if depth == len(word):
                return '#' in node

            if word[depth] == '.':
                for child_char in node.keys():
                    if child_char == '#':
                        continue
                    queue.append(node[child_char])
                    depths.append(depth + 1)
            else:
                if word[depth] not in node:
                    continue
                queue.append(node[word[depth]])
                depths.append(depth + 1)

        return False


# hash map letter + position
class AnotherWrongWordDictionary:
    def __init__(self):
        self.index = [{} for i in range(25)]
        # [
        #     {
        #         'b': {'bad'},
        #         'd': {'dad'},
        #         'm': {'mad'}
        #     },
        #     {
        #         'a': {'bad', 'mad', 'dad'}
        #     },
        #     {
        #         'd': {'bad', 'mad', 'dad'}
        #     }
        # ]

    def addWord(self, word: str) -> None:
        char_position = 0
        for char in word:
            char_position += 1
            if char not in self.index[char_position].keys():
                self.index[char_position][char] = set()
            self.index[char_position][char].add(word)

        print(word, self.index)

    def search(self, word: str) -> bool:
        intersection = None
        char_position = 0
        for char in word:
            char_position += 1
            if char == '.':
                if not self.index[char_position]:
                    return False
                continue

            if char not in self.index[char_position].keys():
                return False

            if intersection is None:
                intersection = self.index[char_position][char]
            else:
                intersection = self.index[char_position][char].intersection(intersection)

            if len(intersection) == 0:
                return False

        if len(intersection) == 0:
            return False

        if intersection is None:
            return True

        for candidate_word in intersection:
            if len(candidate_word) != len(intersection):
                continue
            return True
        return False


# hash map with generating all possible search word
class WrongWordDictionary:  # wrong solution (Time Limit Exceeded)

    def __init__(self):
        self.words = dict()

    def addWord(self, word: str) -> None:
        self.words[word] = word

    def search(self, word: str) -> bool:
        searching_words = self._generate_searching_words(word)
        return self._search_existence_array(searching_words)

    def _search_existence_array(self, words: list) -> bool:
        for word in words:
            if word in self.words.keys():
                return True
        return False

    def _generate_searching_words(self, word: str) -> list:
        searching_words = []
        number_of_wild_cards = 0

        for char in word:
            if char == '.':
                number_of_wild_cards += 1

        for combinations in self._get_n_word_letters(number_of_wild_cards):
            new_word = word
            for combination in combinations:
                new_word = new_word.replace('.', combination, 1)
            searching_words.append(new_word)

        return searching_words

    # from Chat GPT
    @staticmethod
    def _get_n_word_letters(n):
        import string
        import itertools
        return [''.join(i) for i in itertools.product(string.ascii_lowercase, repeat=n)]


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
wordDictionary.search("pad")  # return False
wordDictionary.search("bad")  # return True
wordDictionary.search(".ad")  # return True
wordDictionary.search("b..")  # return True
