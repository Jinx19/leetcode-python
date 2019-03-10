class TrieNode:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.c = None
        self.children = {}
        self.isLeaf = None

    def __init__(self, c):
        """
        Initialize your data structure here.
        """
        self.c = c
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
        children = root.children
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
        t =

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

    def
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
