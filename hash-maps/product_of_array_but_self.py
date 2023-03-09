from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, answer = len(nums), [1] * len(nums)
        
        prefix = 1
        postfix = 1

        for i in range(n):
            answer[i] *= prefix
            prefix *= nums[i]
            answer[-1-i] *= postfix
            postfix *= nums[-1-i]

            # answer[0] = 1*1 = 1
            # [1,1,1,1]
            # prefix = 1*1 = 1
            # answer[-1]//answer[3] = 1*1 = 1
            # [1,1,1,1]
            # postfix = 4*1 = 4

            # [1,1,1,1]

            # answer[1] = 1*1 = 1
            # [1.1.1.1]
            # prefix = 2*1 = 2
            # answer[-2]//answer[2] = 1*4 = 4
            # [1.1.4.1]
            # postfix = 4*3 = 12
            
            # [1,1,4,1]

            # answer[2] = 4*2 = 8
            # [1,1,8,1]
            # prefix = 3*2 = 6
            # answer[-3]//answer[1] = 1*12 = 12
            # [1,12,8,1]
            # postfix = 12*2 = 24

            # [1,12,8,1]

            # answer[3] = 1*6 = 6
            # [1,12,8,6]
            # prefix * 6*4
            # answer[-4]//answer[0] = 1*24 = 24
            # [24,12,8,6]
            # postfix = 24*1 = 24

            # [24.12.8,6]

        return answer



r = Solution().productExceptSelf([1,2,3,4])
print(r)
