class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = [0] * 26
        for char in s:
            i = ord(char) - ord('a')
            letters[i] += 1
        for char in t:
            i = ord(char) - ord('a')
            letters[i] -= 1
        for letter in letters:
            if letter != 0:
                return False
        return True

        