from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberMap = {}
    
        for i, n in enumerate(nums):
            targetDiff = target - n

            if targetDiff in numberMap:
                return [numberMap[targetDiff], i]
            numberMap[n] = i