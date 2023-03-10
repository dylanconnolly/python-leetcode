from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in nums: # indicates start of sequence since neighbor below doesnt exist
                seqLength = 1 # seq is at least length 1
                
                while seqLength + n in nums:
                    seqLength += 1
                
                longest = max(longest, seqLength)
        
        return longest

r = Solution().longestConsecutive([100,4,200,1,3,2])
r2 = Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1])
print(r)
print(r2)