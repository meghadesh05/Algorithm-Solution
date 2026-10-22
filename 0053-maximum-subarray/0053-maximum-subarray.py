class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        maxi = float("-inf")
        total = 0

        for i in range(0, n):
            total = total + nums[i]

            if total> maxi:
                maxi = total

            if total<0 :
                total = 0
        return maxi            