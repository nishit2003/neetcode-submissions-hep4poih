class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mapp = defaultdict(list)
        for c in strs:
            count = [0] * 26
            for s in c:
                count[ord(s) - ord('a')]+=1

            mapp[tuple(count)].append(c)

        return mapp.values()