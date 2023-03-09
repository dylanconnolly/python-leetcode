from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        freqCount = defaultdict(int)

        for n in nums:
            freqCount[n] += 1

        for num, count in freqCount.items():
            freq[count].append(num)

        kMostFrequent = []

        for numArray in reversed(freq):
            for n in numArray:
                kMostFrequent.append(n)

            if len(kMostFrequent) == k:
                return kMostFrequent

r = Solution().topKFrequent([1,1,1,2,2,2,3], 2)
print(r)