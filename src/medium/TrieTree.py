from typing import Optional


class Node:
    def __init__(self, val: Optional[str] = None):
        self.val = val
        self.children = set()
        self.end_of_word_flag = False

    def add_child(self, child):
        self.children.add(child)

    def get_children(self) -> list:
        return list(self.children)

    def word_ends_here(self):
        self.end_of_word_flag = True

    def __repr__(self):
        return str(self.val) + ' -> (' + ','.join(map(str, self.children)) + ')'


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        for i in range(1, len(word) + 1):
            sub_str = word[:i]
            # print(node, sub_str)
            node = self._get_or_create_node(node, sub_str)

        node.word_ends_here()

        return None

    def search(self, word: str) -> bool:
        node = self.root

        for i in range(1, len(word) + 1):
            sub_str = word[:i]
            node = self._find_node(node, sub_str)

            if node is None:
                return False

        # print(node)
        return node is not None and (node.end_of_word_flag or not node.children)

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for i in range(1, len(prefix) + 1):
            sub_str = prefix[:i]
            node = self._find_node(node, sub_str)

            if node is None:
                return False

        # print(node)
        return node is not None

    @classmethod
    def _get_or_create_node(cls, node: Node, word: str) -> Node:
        old_node = cls._find_node(node, word)

        if old_node is not None:
            return old_node

        new_node = Node(word)
        node.add_child(new_node)

        return new_node

    @classmethod
    def _find_node(cls, node: Node, word) -> Optional[Node]:
        for child in node.children:
            child: Node
            if child.val == word:
                return child

        return None

    def __repr__(self):
        return self.root.__repr__()


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# print('init:', obj)
# obj.insert('word')
# print('insert:', obj)
# param_2 = obj.search('word')
# print(param_2)
# param_3 = obj.startsWith('prefix')
# print(param_3)

if __name__ == "__main__":
    obj = Trie()

    while True:
        # print(obj)

        command: str = input('trie tree >> ')

        if command == 'exit':
            break
        if command.startswith('insert'):
            args = command.split()

            obj.insert(args[1])

            continue
        if command.startswith('search'):
            args = command.split()

            print(obj.search(args[1]))

            continue
        if command.startswith('startsWith'):
            args = command.split()

            print(obj.startsWith(args[1]))

            continue

        print('you can only use exit, insert, search and startsWith commands')
