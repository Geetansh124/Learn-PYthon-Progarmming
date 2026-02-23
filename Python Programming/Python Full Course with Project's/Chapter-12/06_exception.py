try:
    a = int(input("Hey, Enter a number: "))
    print(a)
except ValueError as v:
    print("This is a ValueError")
    print(v)

except Exception as e:
    print(e)
print("Thanks You")        

# try:
#     # Code except ZeroDivisionError:
# # Code
# except TypeError:
#     # Code
# except ZeroDivisionError:
#     # Code

# except:
# # Code # All other exceptions are handled here.