instring = input("Would you like to convert to ROT-47 or from ROT-47? ")
while (instring[0] not in "TtFf"):
    instring = input("Would you like to convert to ROT-47 or from ROT-47? ")
print("Input what you would like to convert:")
print()
instring = input()

newstring = ""
num = 0

for x in range(len(instring)):
    num = ord(instring[x])
    if (num > 126 or num < 33):
        newstring = newstring + instring[x]
    else:
        num += 47 - 33
        num = num%94
        num += 33
        newstring = newstring + chr(num)
print()
print()
print()
print(newstring)
print()
print()
print()
instring = input("Press enter to exit")
