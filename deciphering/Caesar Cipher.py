instring = input("Would you like to convert to Caesar Cipher or from Caesar Cipher? ")
while (instring[0] not in "TtFf"):
    instring = input("Would you like to convert to Caesar Cipher or from Caesar Cipher? ")
tofrom = ""
if (instring[0] in "Tt"):
    tofrom = "to"
else:
    tofrom = "from"
shift = int(input("What is the shift to the Caesar Cipher? "))
while (shift < -26 or shift > 26):
    shift = int(input("What is the shift to the Caesar Cipher? "))
print("Input what you would like to convert:")
print()
instring = input()

array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
newstring = ""
num = 0

if (tofrom == "to"):
    for x in range(len(instring)):
        num = ord(instring[x])
        if (instring[x] not in array):
            newstring = newstring + instring[x]
        else:
            newstring = newstring + array[(array.index(instring[x])+shift)%26]

elif (tofrom == "from"):
    for x in range(len(instring)):
        num = ord(instring[x])
        if (instring[x] not in array):
            newstring = newstring + instring[x]
        else:
            newstring = newstring + array[(array.index(instring[x])-shift+26)%26]
print()
print()
print()
print(newstring)
print()
print()
print()
instring = input("Press enter to exit")
