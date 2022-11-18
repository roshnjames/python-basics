l1=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
    ele=int(input("enter the element"))
    l1.append(ele)

print("entered list is ",l1)

print("printing positive numbers only")
print([x for x in l1 if x>0])


l2=['a','e','i','o','u']
str=input("enter your word")
print("printing the vowels present in the eneterd word")
print([x for x in str if x in l2])
print("ordinal value of the word")
print([ord(x) for x in str])
