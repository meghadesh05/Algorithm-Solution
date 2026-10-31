class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        n=len(nums)
        nums.sort()

        for i in range(0, n):
            # Skip duplicate elements
            if i != 0 and nums[i] == nums[i-1]:
                continue

            #Moving the 2 pointers 
            j = i+1
            k = n-1

            while j<k:
                total_sum = nums[i]+nums[j] +nums[k]

                if total_sum <0:
                    j+=1

                elif total_sum >0:
                    k -=1

                else:
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)

                    j+=1
                    k-=1

                    #Skip duplicates for j
                    while j<k and nums[j] == nums[j-1]:
                        j+=1

                    #Skip duplicates for k
                    while j<k and nums[k] == nums[k+1]:
                        k -=1
        return ans                              