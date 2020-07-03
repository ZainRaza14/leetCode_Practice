from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lenS, lenP = len(s), len(p)
        if lenS < lenP:
            return []
        
        count_P = Counter(p)
        count_S = Counter()
        
        result = []
        
        #
        for i in range(lenS):
            count_S[s[i]] += 1
            if i >= lenP:
                if count_S[s[i-lenP]] == 1:
                    del count_S[s[i-lenP]]
                else:
                    count_S[s[i-lenP]] -= 1
                    
            if count_P == count_S:
                result.append(i - lenP + 1)
                
        return result
    
    
        
        
    
        
        