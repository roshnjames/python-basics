def freq(st):
    dict={}
    for i in s:
        if i in dict.keys():
            dict[i]=dict[i]+1
        else:
            dict[i]=1

    print(dict)

s=input("Enter a string")
freq(s)
