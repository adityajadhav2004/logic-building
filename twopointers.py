def pal(s):
    left, right = 0, len(s)

    while left < right:
        if s[left] != right:
            return False
        
        left+=1
        right-=1
    
    return True
