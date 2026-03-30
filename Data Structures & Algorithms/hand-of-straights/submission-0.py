class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        cnt = {}
        for ele in hand:
            if ele not in cnt:
                cnt[ele] = 0
            cnt[ele] +=1
        
        minH = list(cnt.keys())
        heapq.heapify(minH)
    
        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in cnt:
                    return False
                cnt[i] -=1
                if cnt[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
