d={'k1':1,'k2':2,'k3':3}
print(d)
car={'company':'BMW',
     'model':'v3','color':'red','year':2015}
print(car)
print(car['model'])
print(len(car))
print(car.values)


#duplicate value printing
d1={'a1':1,'a2':2}
d2={'a1':3,'a2':4}
d3={**d1,**d2}
for k,v in d3.items():
    if k in d1 and k in d2:
        d3[k]=[v,d1[k]]
print(d3)



print("reading dictionaries")
dict1={}
n=int(input("Enter number of items"))
for i in range(0,n):
      key=input("enter the key")
      value=input("enter the value")
      dict1[key]=value
print(dict1)


print("two dictionaries")
dict2={}
n=int(input("Enter number of items for second dictionary"))
for i in range(0,n):
      key=input("enter the key")
      value=input("enter the value")
      dict2[key]=value
print(dict2)

print("merging")
dict2.update(dict1)
print(dict2)
m=len(dict2)


    

