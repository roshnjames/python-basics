import string
def longst(l):
    str1=""
    st="" 
    for i in l:
        st=i
        if(len(st)>len(str1)):
            str1=st
    print(len(str1))
            

n=int(input("Enter the number of words"))
l=[]
for i in range(0,n):
    w=input("Enter a word")
    l.append(w)
    
longst(l)

    
