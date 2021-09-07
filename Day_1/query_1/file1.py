try:
    fl = open("sampletext.txt","r")
    words = []
    for line in fl:
        for word in line.split():
            words.append(word)
    words = sorted(list(set(words)))
    words.sort(key = len)
    #print(words)
    f = open("newfile.txt","w")
    for i in words:
        f.write("%s\n" %(i+" "+str(len(i))))
except:
    print("Error")
