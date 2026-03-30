"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])
        s,e = 0 ,0 

        curr,res = 0,0
        while s < len(start):
            if start[s] < end[e]:
                curr+=1
                s+=1
            else:
                curr-=1
                e+=1
            res = max(res,curr)
        return res


        
