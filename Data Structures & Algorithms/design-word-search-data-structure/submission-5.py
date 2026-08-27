class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = TrieNode()
            curr = curr.nodes[c]
        curr.is_end = True

    def search(self, word: str) -> bool:

        def dfs(index, node) -> bool:
            curr = node

            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    for child in curr.nodes.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.nodes:
                        return False
                    curr = curr.nodes[char]

            return curr.is_end

        return dfs(0, self.root)