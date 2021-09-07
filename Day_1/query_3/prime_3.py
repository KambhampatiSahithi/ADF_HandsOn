from time import sleep

def isprime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n = int(input())
for i in range(1,n+1):
    if(isprime(i)):
        print(i)
        sleep(5)