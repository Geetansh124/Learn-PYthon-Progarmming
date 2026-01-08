marks = {
    "Geetansh": 100,
    "Ashish": 38,
    "Karan": 17,
}


# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Karan": 52, 0 : "Hello"})
# print(marks)

print(marks.get("Ashish2")) # Prints None if key not found
print(marks["Ashish"]) # Returns an error error if key not found