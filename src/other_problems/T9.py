class T9(object):
    def __init__(self):
        self.dictionary = []
        self.trie = dict()

    def add_to_dictionary(self, word: str, weight: int) -> None:
        serial = self._get_serial_from_word(word)
        word_id = len(self.dictionary)
        self.dictionary.append({
            'word': word,
            'weight': int(weight),
        })

        node = self.trie
        for number in serial:
            if number not in node:
                node[number] = dict()

            node = node[number]

            if '@' not in node:
                node['@'] = []

            node['@'].append(word_id)

    def search(self, serial: str) -> None:
        for i in range(len(serial)):
            if serial[i] == '1':
                break
            print(self._search(serial[:i + 1]))

    def _get_serial_from_word(self, word: str) -> str:
        return ''.join([self._get_key_of_char(char) for char in word])

    def __repr__(self):
        return 'dictionary: ' + str(self.dictionary) + '\n' + 'trie: ' + str(self.trie)

    @staticmethod
    def _get_key_of_char(char: str) -> str:
        numbers = '22233344455566677778889999'
        return numbers[ord(char) - ord('a')]

    def _search(self, serial: str) -> str:
        node = self.trie
        for number in serial:
            if number not in node:
                return 'MANUALLY'
            node = node[number]

        # if node is None:
        #     return self._basic_convert(serial)

        # print(node)
        ids = node['@']
        best_mache = self._find_best_search(ids)

        return best_mache[:len(serial)]

    def _find_best_search(self, ids: list):
        max_weight = 0
        best_word = None

        for i in ids:
            if self.dictionary[i]['weight'] > max_weight:
                max_weight = self.dictionary[i]['weight']
                best_word = self.dictionary[i]['word']

        return best_word


if __name__ == '__main__':
    for _ in range(int(input())):
        t9 = T9()
        for _ in range(int(input())):
            word, weight = input().split(' ')
            t9.add_to_dictionary(word, weight)

        # print(t9)

        for _ in range(int(input())):
            t9.search(input())
