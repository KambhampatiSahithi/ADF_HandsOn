try:
    d = int(input())
    ch= int(input())
    print("choose \n")
    print("1.Binary\n 2.Octal\n 3.Hexadecimal\n")
    if ch==1:
        print(bin(d))
    elif ch==2:
        print(oct(d))
    elif ch==3:
        print(hex(d))
    else:
        print("Choose available options.\n")
except ValueError:
    print("Error in value")
