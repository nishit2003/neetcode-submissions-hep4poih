class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for char in word:
                adj[char] = set()

        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            minlen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        print(adj)

        visit = {}
        res = []

        def dfs(node):
            if node in visit:
                return visit[node]
            
            visit[node] = False
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visit[node] = True
            res.append(node)
            return True
        
        for char in adj:
            if not dfs(char):
                return ""
        res = res[::-1]
        return "".join(res)
