"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#            s
# start =0,5,15
# end = 40,10,20
#        e
# curr = 2 
# max = 2
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        s,e = 0,0
        curr,maxroom = 0,0
        while s <= len(start)-1:
            if start[s] < end[e]:
                curr+=1
                s+=1
            else:
                curr-=1
                e+=1
            maxroom = max(curr,maxroom)
        return maxroom