class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        rows, cols = len(board), len(board[0])
        res = set()
        visit = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(r,c,node,word):
            if (r<0 or c<0 or r>= rows or c >= cols or board[r][c] not in node.children or (r,c) in visit):
                return 
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isEnd:
                res.add(word)
            for dr,dc in directions:
                dfs(r+dr,c+dc,node,word)
            visit.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)
