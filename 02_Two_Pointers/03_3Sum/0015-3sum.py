class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            # Skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left and right values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result



# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         n = len(nums)
#         res = set()                # store unique triplets as tuples

#         for i in range(n):
#             a = nums[i]
#             if i > 0 and a == nums[i - 1]:   # skip duplicate 'a'
#                 continue

#             seen = set()           # values seen while scanning for this 'a'
#             target = -a
#             for j in range(i + 1, n):
#                 need = target - nums[j]
#                 if need in seen:
#                     # (a <= need <= nums[j]) because array is sorted and 'need' came from earlier j
#                     res.add((a, need, nums[j]))
#                 seen.add(nums[j])

#         return [list(t) for t in res]


        
