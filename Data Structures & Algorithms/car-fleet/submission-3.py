class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        pair = [[p,s] for p,s in zip(position,speed)]

        for p,s in sorted(pair)[::-1]:
            time = (target - p)/s
            stack.append(time)

            while len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


# stack = [3,3]

# stack = [(4,2),(1,2),(0,1),(7,1)]

# stack = [(7,1),(4,2),(1,2),(0,1)]
# stack = [(3),(3),(4.5),(10)]
