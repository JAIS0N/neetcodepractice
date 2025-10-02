class Solution(object):
   if not nums:
            return 0
        nums.sort()
        
        longest = 1
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                # skip duplicates
                continue
            if nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                # streak broken, update longest
                longest = max(longest, curr)
                curr = 1   # reset streak

        return max(longest, curr)

        
