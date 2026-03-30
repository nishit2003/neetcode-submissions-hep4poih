class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        patterns = {}
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                if pattern not in patterns:
                    patterns[pattern] = []
                patterns[pattern].append(word)

        q = deque([beginWord])
        res = 1
        visit = set([beginWord])
        while q:
            size = len(q)
            for i in range(size):
                temp = q.popleft()
                if temp == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = temp[:j] + "*" + temp[j+1:]
                    for nei in patterns[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)

            res +=1
        return 0
