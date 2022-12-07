def ing(st):
    if(st[-1]=='g' and st[-2]=='n' and st[-3]=='i'):
        st=st+"ly"
        print(st)
    else:
        st=st+"ing"
        print(st)


s=input("ENter a string")
ing(s)


