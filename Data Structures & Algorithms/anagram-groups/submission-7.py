class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")] += 1
            anagrams[tuple(count)].append(s)
        # res = []
        # for key,val in anagrams.items():
        #     res.append(val)
        # return res
        return list(anagrams.values())

