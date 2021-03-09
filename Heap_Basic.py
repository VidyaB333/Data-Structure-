##Stack implemetation using list in python

class stack:
    def __init__(self):
        self.stack = []

    def append(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def getstack(self):
        return self.stack

s = stack()
print('Printing stack : ', s.getstack())
s.append(110)
s.append(12)
print('Printing stack : ', s.getstack())
s.pop()
print('Printing stack : ', s.getstack())


## Stack Implementation using deque in Python
from collections import deque
a = deque()
a.append('p')
a.appendleft('1')
a.append('m')
print(a)
print(a.pop())
print(a)



