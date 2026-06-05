class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        i = 0
        pre_prod = 1
        post_prod = 1
        while i < len(nums):
            pre_prod = pre_prod * nums[i]
            i = i + 1
            prefix.append(pre_prod)
        j = len(nums)-1
        while j >= 0:
            post_prod = post_prod * nums[j]
            j = j - 1
            postfix.append(post_prod)
        postfix = postfix[::-1]
        output = [1] * len(nums)
        for i in range(len(nums)):
            left = prefix[i - 1] if i - 1 >= 0 else 1
            right = postfix[i + 1] if i + 1 < len(nums) else 1
            output[i] = left * right
        return output




