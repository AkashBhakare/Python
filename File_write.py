# f = open ("write.txt", "w")
# a = f.write("Akash bhai bhauat aache hai\n")
# print(a)
# f.close()


# f = open ("write.txt", "a")
# a = f.write("Akash bhai bhauat aache hai\n")
# print(a)
# f.close()

# handle read and write both

f = open("write.txt", "r+")
print(f.read())
f.write("Thank You")

f.close()