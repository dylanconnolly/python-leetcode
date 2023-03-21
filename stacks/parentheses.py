class Solution:
    def isValid(self, s: str) -> bool:
        r = []

        charMap = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for char in s:
            if char in charMap:
                if len(r) < 1:
                    return False
                
                last = r.pop()
                if last == charMap[char]:
                    continue
                else:
                    return False
            else:
                r.append(char)
        
        return (len(r) == 0)
            

print(Solution().isValid('([{}])'))
print(Solution().isValid('([[{}])]'))