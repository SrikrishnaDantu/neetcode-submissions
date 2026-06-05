class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            length = str(len(s))
            encoded += length + "#" + s
        print(encoded)
        return encoded
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j + 1: j + length + 1]
            decoded.append(word)
            i = j + 1 + length
        return decoded
