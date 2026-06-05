class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            length = len(strs[i])
            strs[i] = str(length) + "#" + strs[i]
        encoded = "".join(strs)
        return encoded 

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            strs.append(word)
            i = j + 1 + length
        return strs
            

