class Solution:
    def isHappy(self, n: int) -> bool:
        nums = [int(digit) for digit in str(n)]
        seen = set()
        total = 0
        while 1 not in seen:
            for num in nums:
                total += num ** 2
            if total in seen:
                return False
            seen.add(total)
            nums = [int(digit) for digit in str(total)]
            total = 0
        return True


        
            


        