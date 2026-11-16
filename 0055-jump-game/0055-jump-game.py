class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_Reach = 0

        for i in range(len(nums)):
            if i> max_Reach:
                return False
            max_Reach = max(max_Reach, i + nums[i])
        return True         