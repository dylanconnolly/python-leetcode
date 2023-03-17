from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers left and right
        l, r = 0, len(height) - 1
        area = 0

        while l < r:
            h = min(height[l], height[r])
            calcArea = h * (r-l)
            if calcArea > area:
                area = calcArea
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area

def test(arr):
    print(Solution().maxArea(arr))

# test([1,8,6,2,5,4,100,3,7])
test([4,3,2,1,4])


