from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            maxProfit = max(maxProfit, price - lowest)
        return maxProfit


def test(prices):
    print(Solution().maxProfit(prices))


test([7,1,5,3,6,4])