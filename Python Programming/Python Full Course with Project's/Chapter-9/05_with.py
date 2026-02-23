# f = open("myfile.txt", "a")
# f.write(st)
# f.close()

#The same code using 'with' statement
with open("myfile.txt", "w") as f:
    print(f.read())

#You don't need to explicitly close the file when using 'with' statement    