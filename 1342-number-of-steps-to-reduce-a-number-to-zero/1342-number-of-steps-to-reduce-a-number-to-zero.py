class Solution:
    def numberOfSteps(self, num: int) -> int:
        count =0 
        while num>0:
            if num % 2 == 0:
                num = num//2
            else: 
                num = num - 1  
            count+=1          
        return count       

        #TC => O(log n) for the repated having process with odd numbers
        #SC => O(1)