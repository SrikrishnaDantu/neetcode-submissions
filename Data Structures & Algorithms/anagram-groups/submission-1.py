from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                count[i] += 1
            if tuple(count) not in res:
                res[tuple(count)] = [s]
            else:
                res[tuple(count)] += [s]
        return list(res.values())


        
            
        