class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)

        adj = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                if pattern not in adj:
                    adj[pattern] = [] 
                adj[pattern].append(word)
        print(adj)
        seen = set()
        q = deque([beginWord])
        level = 1
        while q:
            size = len(q)
            
            for i in range(size):
                word = q.popleft()
                if word == endWord:
                    return level
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in adj[pattern]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
            level+=1
        return 0



