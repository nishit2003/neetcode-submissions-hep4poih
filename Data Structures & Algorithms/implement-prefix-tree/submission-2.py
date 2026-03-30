class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for ele in word:
            if ele not in curr.children:
                curr.children[ele] = Node()
            curr = curr.children[ele]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ele in word:
            if ele not in curr.children:
                return False
            curr = curr.children[ele]
        return curr.end
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ele in prefix:
            if ele not in curr.children:
                return False
            curr = curr.children[ele]
        return True
        