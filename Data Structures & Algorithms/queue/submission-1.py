class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        self.prev = None
        
class Deque:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        temp = Node(value)
        last = self.tail.prev
        self.tail.prev = temp
        temp.prev = last
        last.next = temp
        temp.next = self.tail

    def appendleft(self, value: int) -> None:
        temp = Node(value)
        first = self.head.next

        self.head.next = temp
        temp.next = first
        first.prev = temp
        temp.prev = self.head
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last = self.tail.prev
        val = last.val
        prv = last.prev

        prv.next = self.tail
        self.tail.prev = prv
        
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        first = self.head.next
        val = first.val
        second = first.next

        self.head.next = second
        second.prev = self.head

        return val

