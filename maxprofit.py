#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            profit = 0
            if prices is []:
                return 0
            for i,j in enumerate(prices):
                print(i,j)
                if i == len(prices) - 1:
                    return profit
                else:
                    if prices[i+1] - j> 0:
                        profit += prices[i+1] - j
