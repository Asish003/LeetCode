prices =[2,1,2,0,1]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_cost = float('inf')

        current_cost = 0

        for i in range(len(prices)): 
            current_cost = prices[i]

            if current_cost < min_cost: 
                min_cost = current_cost

            if current_cost - min_cost > max_profit: 
                max_profit = current_cost - min_cost

        print(max_profit)
        print(min_cost)

        return max_profit