class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for h in range(i+1, len(nums)):
                if nums[i] + nums[h] == target:
                    return [i, h]
       
