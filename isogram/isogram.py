import re

def is_isogram(string):
    seen = []

    for char in string.lower():
        skip = re.compile(r'\W').match(char)
        
        if (skip):
            continue

        if (char in seen):
            return False
        
        seen.append(char)

    return True
