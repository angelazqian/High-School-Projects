intofrom = input("Would you like to convert to binary or from Octal? ")
while (intofrom[0] not in "FfTt"):
    intofrom = input("Would you like to convert to binary or from Octal? ")
tofrom = ""
if (intofrom[0] in "Tt"):
    tofrom = "to"
else:
    tofrom = "from"
print ("Input what you would like to convert:")
print ()
instring = input()

newstring = ""
num = 0

if (tofrom == "to"):
    for x in range(len(instring)):
        num = ord(instring[x])
        newstring = newstring + str(num//64)
        num = num%64
        newstring = newstring + str(num//8) + str(num%8) + " "
    
elif (tofrom == "from"):
    while (len(instring) > 0):
        num = (64 * int(instring[0])) + (8 * int(instring[1])) + int(instring[2])
        newstring = newstring + chr(num)
        instring = instring[3: len(instring)]
        while (len(instring) > 0 and instring[0] == " "):
            instring = instring[1: len(instring)]
        

print()
print()
print()
print(newstring)
print()
print()
print()
tofrom = input("Press enter to exit")
