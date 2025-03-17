intofrom = input("Would you like to convert to Base64 or from Base64? ")
while (intofrom[0] not in "TtFf"):
    intofrom = input("Would you like to convert from Base64 or from Base64? ")
tofrom = ""
if (intofrom[0] in "Tt"):
    tofrom = "to"
else:
    tofrom = "from"
print("Input what you would like to convert:")
print()
instring = input()

newstring = ""              #to be outputted
binstring = ""              #is what string is when in binary
num = 0


if (tofrom == "to"):
    for x in range(len(instring)):
        num = ord(instring[x])
        for y in range (8):
            binstring = binstring + str(int(num/(2**(7-y))))
            num = num%(2**(7-y))
    while (len(binstring)%6 != 0):
        binstring = binstring + "0"
    while (len(binstring) > 0):
        num = 0
        for x in range(6):
            num = num + int(binstring[x])*(2**(6-x-1))
        binstring = binstring[6: len(binstring)]
        if (num < 26):
            newstring = newstring + chr(num + 65)
        elif (num < 52):
            newstring = newstring + chr(num + 71)
        elif (num < 62):
            newstring = newstring + chr(num - 4)
        elif (num == 62):
            newstring = newstring + "+"
        elif (num == 62):
            newstring = newstring + "/"
    while (len(newstring)%4 != 0):
        newstring = newstring + "="
    print()
    print()
    print()
    print(newstring)

elif (tofrom == "from"):
    while (instring[-1] == "="):
        instring = instring[:-1]
    for x in range(len(instring)):
        num = 0
        if (ord(instring[x]) > 47) and (ord(instring[x]) < 58):
            num = ord(instring[x])+4
        elif (ord(instring[x]) > 96) and (ord(instring[x]) < 123):
            num = ord(instring[x]) - 71
        elif (ord(instring[x]) > 64) and (ord(instring[x]) < 91):
            num = ord(instring[x]) - 65
        elif (instring[x] == "+"):
            num = 62
        elif (instring[x] == "/"):
            num = 63
        for y in range (6):
            binstring = binstring + str(int(num/(2**(5-y))))
            num = num%(2**(5-y))
    while (len(binstring)%8 != 0):
        binstring = binstring[:-1]
    while (len(binstring) > 0):
        num = 0
        for x in range(8):
            num = num + int(binstring[x])*(2**(7-x));
        binstring = binstring[8: len(binstring)]
        newstring = newstring + chr(num)
    print(newstring)
print()
print()
print()
tofrom = input("Press enter to exit")
























