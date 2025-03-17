instring = input("Would you like to convert to ROT-13 or from ROT-13? ")
while (instring[0] not in "TtFf"):
    instring = input("Would you like to convert to ROT-13 or from ROT-13? ")
print("Input what you would like to convert:")
print()
instring = input()

array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
newstring = ""
num = 0

for x in range(len(instring)):
    num = ord(instring[x])
    if (instring[x] not in array):
        newstring = newstring + instring[x]
    else:
        newstring = newstring + array[(array.index(instring[x])+13)%26]

print()
print()
print()
print(newstring)
print()
print()
print()
instring = input("Press enter to exit")
