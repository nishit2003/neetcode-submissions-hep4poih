class StringIterator:

    def __init__(self, compressedString: str):
        self.queue=collections.deque() # stores: char, count
        self.currChar=""
        self.currCounter=0
        substr=""
        for i in range(0,len(compressedString)):
            if i>0 and not compressedString[i].isdigit():
                self.queue.append((substr[0], int(substr[1:])))
                substr=""
            substr+=compressedString[i]
        self.queue.append((substr[0], int(substr[1:])))
        print(self.queue)
            

    def next(self) -> str:
        if self.hasNext() and self.currCounter==0:
            self.currChar, self.currCounter = self.queue.popleft()
        self.currCounter-=1
        return self.currChar


    def hasNext(self) -> bool:
        if self.currCounter or self.queue:
            return True
        return False



# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()