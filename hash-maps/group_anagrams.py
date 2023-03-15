from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        
        for string in strs:
            alphabetized = ''.join(sorted(string))
            if alphabetized in hash:
                hash[alphabetized].append(string)
            else:
                hash[alphabetized] = [string]
                
        result = []

        for v in hash.values():
            result.append(v)
            
        return result


r = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(r)