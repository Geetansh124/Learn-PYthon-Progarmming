with open("log.html") as f :
    content = f.read()

if ("pyton" in content):
    print("Yes Python is present")

else:
    print("No Python is not present")