class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        n = len(nums)
        for i in range(0, n):
            remaining = target - nums[i]
            if remaining in hash_map:   
                return [hash_map[remaining], i]
            else:
                 hash_map[nums[i]] = i   

        