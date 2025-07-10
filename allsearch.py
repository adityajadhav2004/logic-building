# linear search 
def linearsearch(array,target):
   for i in range(len(array)):
       if array[i] == target:
        return i
   return "not foud"


a = [4, 43, 43, 56,43]
c = linearsearch(a,43)

print(c)