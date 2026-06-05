class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            if num not in res:
                res[num] = 1
            else:
                res[num] += 1
        sorted_res = {key: value for key, value in sorted(res.items(), key=lambda item: item[1], reverse=True)}
        return list(sorted_res.keys())[:k]


        