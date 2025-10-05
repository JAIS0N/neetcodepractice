class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen=[]
        left=0
        right=len(numbers)-1
        while left<right:
            k=numbers[left]+numbers[right]
            if target==k:
                seen.append(numbers[left])
                seen.append(numbers[right])
                return seen
            if target<k:
                right=right-1
            else:
                left=left+1
            
        
