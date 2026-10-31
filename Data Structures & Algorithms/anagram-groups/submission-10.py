class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for ele in word:
                arr[ord(ele) - ord('a')] += 1
            data[tuple(arr)].append(word)
        
        return list(data.values())
