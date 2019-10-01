class TrieNode:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.c = None
        self.children = {}
        self.isLeaf = None


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        children = self.root.children
        for i in range(len(word)):
            c = word[i]

            if c in children:
                t = TrieNode(c)
                children[c] = t
            children = t.children

            if i == len(word) - 1:
                t.isLeaf = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """