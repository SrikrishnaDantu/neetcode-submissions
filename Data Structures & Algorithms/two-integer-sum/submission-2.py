# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

class Solution:
    def twoSum(self, nums:List[int], target: int) ->  List[int]:
        my_dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) not in my_dict:
                my_dict[nums[i]] = i
            else:
                return [my_dict[(target-nums[i])], i]  

