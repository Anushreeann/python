from cgi import print_directory


f=open("test.txt","r")              
print("name of file:",f.name)   #get the name of file
                               #output:file.py
print("closed or not:",f.closed)   #check the file is closed or not return true or false
print("opening mode:",f.mode)       #return r mode
#read into file
print(f.read(7))                #read atmost size bytes from file
print(f.read())                 #read till end 
print(f.readline())            #read and return one line 
f.close()                        

#write into file
F=open("file.txt","w+")
F.write("Everything in python are objects")
print(F.seek(4))                    #sets the current file position 
print(F.readline())
print(F.tell())                     #return current file position
F.close()                           #close the file object

#check python word is present in file
fd=open("test.txt","r+")
if "python" in fd.read():
    print("python is present in file 'test.txt'")
else:
    print("python is present in file 'test.txt'")
