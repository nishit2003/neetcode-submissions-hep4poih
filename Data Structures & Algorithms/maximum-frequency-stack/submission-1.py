class FreqStack:

    def __init__(self):
        self.values=[[]] #each index is a bucket which stores number of elements which appeared i times
        self.freq={} #stores key=number, value=count
        self.maxFreq=0

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val]=0
        self.freq[val]+=1
        if self.freq[val]>=len(self.values):
            self.values.append([val])
        else:
            self.values[self.freq[val]].append(val)
        self.maxFreq=max(self.maxFreq, self.freq[val])

    def pop(self) -> int:
        # print(self.values, self.maxFreq)
        res=self.values[self.maxFreq].pop()
        self.freq[res]-=1
        if len(self.values[self.maxFreq])==0:
            self.maxFreq-=1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()