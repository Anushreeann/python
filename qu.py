queue=[]
queue.append(60)
queue.append(20)
queue.append(30)
queue.extend([40,50])
print("after insertion",queue)
print(len(queue))
queue.pop()
print("first popped",queue)
queue.pop(0)
print("second popped",queue)
queue.pop(1)
print(queue)
print("after deletion",queue)
print(not queue)





