class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        lst = []
        highest = 0
        for num in nums:
            if num not in hashset:
                hashset.add(num)
        for num in nums:
            if (num-1) not in hashset:
                sublst = []
                sublst.append(num)
                lst.append(sublst)
        for sublst in lst:
            for num in sublst:
                if (num + 1) in hashset:
                    sublst.append(num+1)
        for sublst in lst:
            print(len(sublst))
            if len(sublst) > highest:
                highest = len(sublst)
        return highest


        