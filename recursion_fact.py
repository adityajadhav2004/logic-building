def recursion(a):
    if a==0 or a==1:
        return 1
    else:
        return a * recursion(a-1)
    
print(recursion(3))