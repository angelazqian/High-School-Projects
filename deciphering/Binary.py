intofrom = input("Would you like to convert to binary or from binary? ")
while (intofrom[0] not in "FfTt"):
    intofrom = input("Would you like to convert to binary or from binary? ")
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
count = 0

if (tofrom == "to"):
    for x in range (len(instring)):
        num = ord(instring[x])
        for y in range (8):
            newstring = newstring + str(int(num/(2**(7-y))))
            num = num%(2**(7-y))
        newstring = newstring + " "
elif (tofrom == "from"):
    for x in range(len(instring)):
        num = 0
        count = 0
        while (count < 8 and count < len(instring) and instring[count] in "10"):
            count += 1
        for y in range(count):
            num = num + int(instring[y])*(2**(count-1-y))
        instring = instring[count: len(instring)]
        while (len(instring) > 0 and instring[0] == " "):
            instring = instring[1: len(instring)]
        newstring = newstring + chr(num)

print()
print()
print()
print(newstring)
print()
print()
print()
tofrom = input("Press enter to exit")
