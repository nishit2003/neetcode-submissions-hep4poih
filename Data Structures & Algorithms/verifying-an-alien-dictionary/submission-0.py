class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_idx = {c:i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]

            for j in range(min(len(w1),len(w2))):
                if w1[j] != w2[j]:
                    if order_idx[w1[j]] > order_idx[w2[j]]:
                        return False
                    break
            else:
                # Words are identical up to length of w2, but w1 is longer → not sorted
                if len(w1) > len(w2):
                    return False
        return True
