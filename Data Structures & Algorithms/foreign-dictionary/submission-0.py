class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char:set() for word in words for char in word}
        # print(adj)
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        print(adj)

        visited = {} # true: cycle, false : no cycle detected
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True

            for nei in adj[char]:
                if dfs(nei):
                    return True
            
            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)