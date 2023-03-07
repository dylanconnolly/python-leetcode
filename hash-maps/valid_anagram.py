
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    letters = {}

    for char in s:
        print(char)
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    for char in t:
        if char not in letters:
            return False
        if char in letters:
            if letters[char] == 1:
                del letters[char]
            else:
                letters[char] -= 1

    if len(letters) == 0:
        return True
    
    return False


isAnagram('anagram', 'nagaram')