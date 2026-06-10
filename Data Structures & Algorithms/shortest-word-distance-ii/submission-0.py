class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordMap={} # stores list of indices
        self.size=len(wordsDict)
        for i, word in enumerate(wordsDict):
            if word not in self.wordMap:
                self.wordMap[word]=[]
            self.wordMap[word].append(i)
        # print(self.wordMap)

    def shortest(self, word1: str, word2: str) -> int:
        if word1 not in self.wordMap or word2 not in self.wordMap:
            return -1
        elif self.wordMap[word1][-1]<self.wordMap[word2][0]:
            # all word1 appears before word 2
            return self.wordMap[word2][0]-self.wordMap[word1][-1]
        elif self.wordMap[word2][-1]<self.wordMap[word1][0]:
            # all word2 appears before word1
            return self.wordMap[word1][0]-self.wordMap[word2][-1]
        else:
            left, right = 0, 0
            res=self.size
            while left<len(self.wordMap[word1]) and right<len(self.wordMap[word2]):
                diff=self.wordMap[word1][left]-self.wordMap[word2][right]
                res=min(res, abs(diff))
                if diff>0:
                    right+=1
                else:
                    left+=1
            return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
