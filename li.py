a=['red','blue','green',2,1+3,"python"]
print(a)
print(len(a))
a.append("c")
a.insert(3,1)
a.pop(4)
a.remove('c')
print(a[0:3])
a[3]='orange'
print(a)
b=[]
b.extend(['A','B','C'])
print(b)
if 'A' in b:
       print("value exits")
