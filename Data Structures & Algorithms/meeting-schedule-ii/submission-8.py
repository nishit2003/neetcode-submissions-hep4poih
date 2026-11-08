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

        s,e = 0,0
        res = curr = 0
        while s < len(start):
            if start[s] < end[e]:
                s+=1
                curr+=1
            else:
                e+=1
                curr-=1

            res = max(res,curr)
        return res