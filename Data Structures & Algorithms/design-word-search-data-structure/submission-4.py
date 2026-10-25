class Node:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ele in word:
            if ele not in curr.children:
                curr.children[ele] = Node()
            curr = curr.children[ele]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(i,curr):
            if i == len(word):
                return curr.end
            
            elif word[i] == ".":
                for child in curr.children.values():
                    if dfs(i+1,child):
                        return True
                return False

            elif word[i] not in curr.children:
                return False
            
            return dfs(i+1,curr.children[word[i]])

        return dfs(0,self.root)