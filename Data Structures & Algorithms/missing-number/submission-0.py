class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set()
        for i in range(0, len(nums)+1):
            if i not in hashset:
                hashset.add(i)
        result = list(hashset ^ set(nums))
        return result[0]


        