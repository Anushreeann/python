dict=dict()                                   # dictionary  initailisation
dict1={1:"python",2:"c",3:"java"}
print(dict1)
print(dict1.items())                           #to view every key value pair
print(len(dict1))                               #print length
dict1[2]="c++"                                  #update the value
d1={4:"html"}                                   
dict1.update(d1)                                #add item
print("after addition",dict1)
print("language:",dict1.get(1))                #return value for specified key          
print("the popped element is ",dict1.pop(3))    #remove the value pair
print("the dictionary is",dict1)
print(2 in dict1)                                 #return true if key is there
if 2 in dict1:
    print("value of key is:",dict1[2])  
dict2={'dict4':{1:'hello'},'dict3':{'name':"roe"}} 
print(dict2['dict4'])
result=dict2.popitem()                       #remove last insertes item 
print(result)                               #return popitem
mydict={['python']:"language"}
print(mydict)                                  #keys cant be of type that is mutable

