class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            j=i+1
            if j-1<1:
                continue
        return i

        
