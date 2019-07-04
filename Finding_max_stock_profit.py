'''
Given a array of numbers representing the stock prices of a company 
in chronological order, write a function that calculates the maximum 
profit you could have made from buying and selling that stock once. 
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since 
you could buy the stock at 5 dollars and sell it at 10 dollars.
'''

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_val = prices[0]
        max_profit = 0
    
        # Iterating over the given input
        for i in range(len(prices)):
            min_val = min(prices[i],min_val)
            
            # Updating the minimum value till now
            if prices[i] < min_val:
                min_val = prices[i]

            # Updating the maximum profit value till now
            if prices[i] - min_val > max_profit:
                max_profit = prices[i] - min_val
                     
        return max_profit
   
# Taking the input from the user
list1 = Solution()
print(list1.maxProfit([7,1,5,3,6,4]))
#print(list1.maxProfit([7,6,4,3,1]))
