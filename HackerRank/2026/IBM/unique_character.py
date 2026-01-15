def getUniqueCharacter(s):
    for i, char in enumerate(s):
        if s.count(char) == 1:
            return i+1
    return -1
        
print(getUniqueCharacter("statistics"))