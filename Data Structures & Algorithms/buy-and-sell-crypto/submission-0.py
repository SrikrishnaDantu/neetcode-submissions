class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        maximum = 0
        length = len(prices)
        while (right < length):
            if (prices[right] - prices[left]) < 0:
                left += 1
            else:
                profit = prices[right] - prices[left]
                if profit > maximum:
                    maximum = profit
                right += 1
        return maximum
        