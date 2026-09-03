class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = {}
        for word in strs:
            cnt = [0] * 26
            for i in word:
                cnt[ord(i)-ord('a')] += 1
            key = tuple(cnt)
        
            if key not in dict:
                dict[key] = []
            
            dict[key].append(word)
        
        return list(dict.values())

