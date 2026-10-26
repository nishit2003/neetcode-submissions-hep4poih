class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.word = None
    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        seen = set()

        root = TrieNode()
        for word in words:
            root.addWord(word)
        res = set()
        def dfs(r,c,node):
            if r >= rows or r < 0 or c >= cols or c < 0 or (r,c) in seen:
                return 

            ch = board[r][c]
            if ch not in node.children:
                return False
            
            node = node.children[ch]
            seen.add((r,c))

            if node.isEnd:
                res.add(node.word)

            for dr, dc in directions:
                dfs(r+dr, c+dc, node)
            
            seen.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)
        return list(res)
