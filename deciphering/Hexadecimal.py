intofrom = input("Would you like to convert to Hexadecimal or from Hexadecimal? ")
while (intofrom[0] not in "FfTt"):
    intofrom = input("Would you like to convert to Hexadecimal or from Hexadecimal? ")
tofrom = ""
if (intofrom[0] in "Tt"):
    tofrom = "to"
else:
    tofrom = "from"
print ("Input what you would like to convert:")
print ()
instring = input()

array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 0,0,0,0,0,0,0,0,0,0,'a', 'b', 'c', 'd', 'e', 'f']
newstring = ""
num = 0

if (tofrom == "to"):
    for x in range (len(instring)):
        num = ord(instring[x])
        newstring = newstring + array[num//16] + array[num%16] + " "
elif (tofrom == "from"):
    while (len(instring) > 0):
        num = 16 * (array.index(instring[0])%16) + (array.index(instring[1])%16)
        newstring = newstring + chr(num)
        instring = instring[2: len(instring)]
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
