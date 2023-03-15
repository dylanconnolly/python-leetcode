class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create left and right pointer
        leftPtr = 0
        rightPtr = len(s) - 1
        # iterate through array and compare left pointer to right pointer
        while leftPtr <= rightPtr:
            # get char at left and right pointer                
            leftChar = s[leftPtr]
            rightChar = s[rightPtr]
            # if character at index is not a letter, move that pointer forward
            # 48-57 = 0-0
            # 65-90 = A-Z
            # 97-122 = a-z
            if not (47 < ord(leftChar) < 58 or 64 < ord(leftChar) < 91 or 96 < ord(leftChar) < 123):
                leftPtr += 1
                continue
            if not (47 < ord(rightChar) < 58 or 64 < ord(rightChar) < 91 or 96 < ord(rightChar) < 123):
                rightPtr -= 1
                continue
            # compare left pointer to right pointer
            if leftChar.lower() != rightChar.lower():
                # if letters don't match at indexes, return false
                return False
            # if letters are both indexes match, index left +1, index right -1
            leftPtr += 1
            rightPtr -= 1

        # if pointers overlap without having different characters, sentence is palindrome
        return True
            

a = Solution().isPalindrome('A man, a plan, a canal: Panama')
print(a)
b = Solution().isPalindrome('')
print(b)
c = Solution().isPalindrome('race a car')
print(c)
d = Solution().isPalindrome('r a ! Cc aR')
print(d)
e = Solution().isPalindrome('0P')
print(e)