class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        
        max_wealth = 0
        for i in range(0, len(accounts)):
            total = 0
            for j in range(0,len(accounts[i])):
                total += accounts[i][j]
            
            if total > max_wealth:
                max_wealth = total
        return max_wealth    

        # TC => O(m*n)
        #SC => O(1)
