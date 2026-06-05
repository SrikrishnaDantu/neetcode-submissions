class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = 0
        highest = 0
        count = 0
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                count += 1
                if count > highest:
                    highest = count
            else:
                count = 0
                left += 1
                right = left
                seen = set()
            print(seen)
            print(count)
        return highest


        
        