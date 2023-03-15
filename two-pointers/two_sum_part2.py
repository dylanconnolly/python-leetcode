from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # solution can only use constant extra space

        # left and right pointer

        # if left + right is greater than target, move the right pointer

        # if left + right is less than target, move left pointer

        l, r = 0, len(numbers) - 1
        
        while l < r-1:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            while numbers[l] + numbers[r] > target:
                r -= 1
            while numbers[l] + numbers[r] < target:
                l += 1
        return [l+1, r+1]


def test(nums, tar):
    print(Solution().twoSum(nums, tar))

test([2,7,11,15], 9)
test([-1,0], -1)
test([2,3,4], 6)
test([-100,-20,1,2,3,4,5,6], 11)