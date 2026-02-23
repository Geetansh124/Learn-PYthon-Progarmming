f = open("poem.txt")
content = f.read()

if("twinkle" in content):
    print("The twinkle word is present in content")

else:
    print("The twinkle word is not present in content") 

f.close()