class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums.sort()
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                # skip duplicates
                continue
            if nums[i] == nums[i-1] + 1:
                curr += 1

        return curr


        
