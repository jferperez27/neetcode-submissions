class PrefixTree:

    def __init__(self):
        self.nodes = {}
        self.word = False
        

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = PrefixTree()
            curr = curr.nodes[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return curr.word
        
    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return True
        
        