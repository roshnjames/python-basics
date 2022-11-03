str=input("Enter your string")

count=0
ch=input("Enter the word you want to get the count of")
l=[]
l=str.split(" ")
n=len(l)
for i in range(0,n):
    w=l[i]
    if(ch==w):
        count+=1

print("count is ",count)
