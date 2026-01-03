f = open("poem.txt", "w")
content = f.read()

if("twinkle" in content):
    print("The twinkle word is present iin content")

else:
    print("The twinkle word is not present in content") 

f.close()       