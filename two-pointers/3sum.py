from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort input array to avoid duplicates
        nums.sort()
        result = []

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result
                


def test(nums):
    print(Solution().threeSum(nums))


test([-1,0,1,2,-1,-4])
test([0,1,1])
test([0,0,0])