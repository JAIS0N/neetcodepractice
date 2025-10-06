def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                    continue
            l=i+1
            r=len(nums)-1
            while l<r:
                threesum=a+nums[l]+nums[r]
                if threesum>0:
                    r=r-1
                elif threesum<0:
                    l=l+1
                else:
                    res.append([a,nums[l],nums[r]])
                    l=l+1
                    while nums[l]==nums[l-1] and l<r:
                        l=l+1
        return res




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


        
