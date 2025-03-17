instring = input("Would you like to convert to Vigenère Cipher or from Vigenère Cipher? ")
while (instring[0] not in "TtFf"):
    instring = input("Would you like to convert to Vigenère Cipher or from Vigenère Cipher? ")
tofrom = ""
if (instring[0] in "Tt"):
    tofrom = "to"
else:
    tofrom = "from"

validkey = 0
while (validkey == 0):
    print("What is the key to the Vigenère Cipher? ")
    print()
    key = input()
    print()
print()
print("Input what you would like to convert:")
print()
instring = input()
instring = instring.upper()
key = key.upper()

newstring = ""
num = 0
count = 0

if (tofrom == "to"):
    for x in range(len(instring)):
        num = ord(instring[x]) + ord(key[count%len(key)]) - 130
        num = num%26
        num += 65
        if (instring[x] in "QWERTYUIOPASDFGHJKLZXCVBNM"):
            newstring = newstring + chr(num)
            count += 1
        else:
            newstring = newstring + instring[x]
            
elif (tofrom == "from"):
    for x in range(len(instring)):
        num = 26 + ord(instring[x]) - ord(key[count%len(key)])
        num = num%26
        num = num + 65
        if (instring[x] in "QWERTYUIOPASDFGHJKLZXCVBNM"):
            newstring = newstring + chr(num)
            count += 1
        else:
            newstring = newstring + instring[x]
        
    
print()
print()
print()
print(newstring)
print()
print()
print()
instring = input("Press enter to exit")

























