#Array using (Python Array Module)

import array as arr
#also we can use this "from array import *"



val = arr.array('i', [1,2,3,4,5,6])

for i in range(0, 6):
    print(val[i], end=" ")

print('\nThis is the next line ')

for x in val:
    print(x, end= ' , ')



from array import *

print('\nThis is the next array ')

val = array('i', [1,2,3,4,5,6])

for i in range(0, 6):
    print(val[i], end=" ")

print('\nThis is the next array line ')

for x in val:
    print(x, end= ' , ')