import sys
import uuid
from collections import defaultdict
import re

def prefix_to(l):
    c = 0
    for wd in l:
        if wd.startswith("to"):
            c += 1
    return c
def postfix_ing(l):
    c = 0
    for wd in l:
        if wd.endswith("ing"):
            c += 1
    return c
def most_repeated(l):
    tmp = defaultdict(int)
    for wd in l:
        tmp[wd] += 1
    return str(max(tmp,key=tmp.get))
def find_palindrome(l):
    for wd in l:
        if (wd == wd[::-1] and len(wd)>1):
            print(wd,end=" ")
    print()
    return
try:

    with open(sys.argv[1],"r") as fl:
        data = fl.readlines()
    input_list = []
    for line in data:
        input_list.extend(line.split())
    print(input_list)
    print("A.Number of words having prefix with 'To' :",prefix_to(input_list))
    print("B.Number of words having ending with 'ing' :", postfix_ing(input_list))
    print("C.Word that was repeated most of times is: ",most_repeated(input_list))
    print("D.The palindrome present in the file are: ",find_palindrome(input_list))
    print("E. Unique words: ",set(input_list))
    print("F. Word dict with key as counter index and value as the word: ",dict(enumerate(input_list)))

    inp_fl = open(sys.argv[1],"r")
    list_data = list(inp_fl.read().split(" "))
    l=[]
    for i in range(len(list_data)):
        l.extend(re.split('a|e|i|o|u|A|E|I|O|U',list_data[i]))
    for i in range(len(l)):
        if len(l[i]) >= 3:
            l[i].replace(l[i][2],l[i][2].upper(),1)
        if (i+1)%5==0:
            l[i] = l[i].upper()
        l[i] = l[i].replace('\n',';')
    l = " ".join(l).split()
    uniq_flname = str(uuid.uuid4())
    uniq_flname += '.txt'
    with open(uniq_flname,'x') as fl:
        fl.write("-".join(l))
except Exception:
    print("Error Occured")


