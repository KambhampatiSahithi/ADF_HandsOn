import math
try:
    a = int(input())
    b= int(input())
    c = math.gcd(a,b)
except ZeroDivisionError:
    c = 0
print("The GCD of given numbers",c)