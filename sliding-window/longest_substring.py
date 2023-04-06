class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, result = 0, 0
        chars = set()

        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[i])
            result = max(result, i - left + 1)
        
        return result
        

def test(string):
    print(Solution().lengthOfLongestSubstring(string))

test("abcabcbb")
test("abcabcdefa")
test("bbbb")
test("dvdf")