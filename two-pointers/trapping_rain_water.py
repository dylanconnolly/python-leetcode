from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        trapped_water = 0
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                trapped_water += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                trapped_water += right_max - height[r]
        return trapped_water



        

def test(arr):
    print(Solution().trap(arr))

test([0,1,0,2,1,0,1,3,2,1,2,1]) # should equal 6
test([4,2,0,3,2,5]) # should equal 9