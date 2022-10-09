a=[3,7,8,5,1]
print(sorted(a))
print(a)
a.sort()
print(a.sort()) #list method doesn't return any value
print(a)
b=['ar','ddd','mmmm','t']
print(sorted(b,key=len))
print(sorted(b,key=str.lower))
c=[1,"dave",3.14,["mark",7,9,[105,101]]]
print(c[3][0])
print(c[2])
print(c[0])
print(c[3][3])
print(c[:-2])
