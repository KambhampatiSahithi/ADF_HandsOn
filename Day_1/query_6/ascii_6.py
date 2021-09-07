try:
    c = input()
    print("The ASCII value of '"+c+"' is "+str(ord(c)))
except TypeError:
    print("Type error")