import math
arr = []
i = 2
count = 0

while (i<571):
    if (pow(i,286)%557!=1):
         if (pow(i,52)%557!=1):
            if (pow(i,44)%557!=1):
                    arr.append(i)
                    count+=1
    i += 1
    
print(arr)
print("572 has", count, "primitive roots")