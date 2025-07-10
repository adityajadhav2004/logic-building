# write a program to find greatest of three numbers

a = input()
b = input()
c = input()

if a >= b and a >= c:
    print("a is the greatest")

elif a<=b and b>=c:
    print("b is the greatest")

else:
    print("c is the greatest")