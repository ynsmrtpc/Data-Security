import math

x = int(input("number 1: "))
y = int(input("number 2: "))

sol = pow(x,y)

z = int(input("mod: "))

final = sol %  z

print(final)