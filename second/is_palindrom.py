from collections import deque

def is_palindrom(s):
    d =  deque()
    for c in s:
        if c == ' ':
            continue
        d.append(c.lower())
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True