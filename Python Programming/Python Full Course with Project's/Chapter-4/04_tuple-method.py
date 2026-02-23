a = (0,4,4,5,6,7,8,False, "Rohan",1, "Shivam", 23.6, )
b = ("Geetansh Patle", 932.21, 31, 'This is the cod e to find the error')
print(a)
print(type(a))
no = a.count(4)
print(no)

print(a.index(1))
print(a.index(23.6))

i = a.index("Rohan")
print(i)

my_tuple = (1,5,6,7)
print(6 in my_tuple)
print(2 in my_tuple)




n = (21,54,95,4,3)
print(len(n))
a,b,c,d,e = n

print(a,b,c,d,e)
