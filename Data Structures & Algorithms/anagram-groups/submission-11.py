class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)

        for word in strs:
            cnt = [0] * 26
            for ele in word:
                cnt[ord(ele)-ord("a")] += 1
            
            data[tuple(cnt)].append(word)
        
        return list(data.values())