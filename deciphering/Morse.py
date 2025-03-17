intofrom = input("Would you like to convert to Morse or from Morse? ")
while (intofrom[0] not in "TtFf"):
    intofrom = input("Would you like to convert from Morse or from Morse? ")
tofrom = ""
if (intofrom[0] in "Tt"):
    tofrom = "to"
else:
    tofrom = "from"
dot = ""
dash = ""
space = ""

if (tofrom == "from"):
    while (len(dot) != 1):
        dot = input("Input what character you will be using as a dot: ")
    while (len(dash) != 1 or dash == dot):
        dash = input("Input what character you will be using as a dash: ")
    while ((len(space) != 1 or space == dot or space == dash) and space != "   "):
        space = input("Input what character you will be using as a space, or input three spaces: ")
print ("Input what you would like to convert: ")
print()
instring = input()
if (tofrom == "to"):
    instring = instring.upper()
for x in range(len(instring)):
    if (tofrom == "to"):
        if (instring[x] not in "QWERTYUIOPASDFGHJKLZXCVBNM@.,?:/-='()_!&;$1234567890+ " and instring[x] not in '"'):
            print ("String not valid")
            print (x)
            print (instring[x])
            tofrom = input("Press enter to exit ")
            exit()
    elif (tofrom == "from"):
        if (instring[x] != " " and instring[x] != dot and instring[x] != dash and instring[x] != space):
            print ("String not valid")
            tofrom = input("Press enter to exit ")
            exit()

newstring = ""              #to be outputted
possible = ""
num = 0

#                           EISH54V3UF2ARLWPJ1T6NDBXKCYMGZ7QO890


if (tofrom == "to"):
    for x in range(len(instring)):
        if (instring[x] in "AEFHIJLPRSUVW12345.?'_&$@+" or instring[x] in '"'): newstring = newstring + "."
        elif (instring[x] in "BCDGKMNOQTXYZ67890,:/-=()!;"): newstring = newstring + "-"

        if (instring[x] in "BCDFHIKNSUVXY23456?/-=()_!;$"): newstring = newstring + "."
        elif (instring[x] in "AGJLMOPQRWZ01789.,:'&@+" or instring[x] in '"'): newstring = newstring + "-"

        if (instring[x] in 'BDGHLQRSVXZ34567.,/-=&"$+'): newstring = newstring + "."
        elif (instring[x] in "CFJKOPUWY12890?:/'()_!;@"): newstring = newstring + "-"

        if (instring[x] in 'BCFHLPZ45678,-=!&";@'): newstring = newstring + "."
        elif (instring[x] in "JQVXY12390.?/'()_$+"): newstring = newstring + "-"

        if (instring[x] in "56789.?/()&:+-_$"): newstring = newstring + "."
        elif (instring[x] in "01234',?=!@;" or instring[x] in '"'): newstring = newstring + "-"

        if (instring[x] in "?':;$@" or instring[x] in '"'): newstring = newstring + "."
        elif (instring[x] in ".,!)-_"): newstring = newstring + "-"

        if (instring[x] in "$"): newstring = newstring + "-"

        if (instring[x] in " "): newstring = newstring + "/"
        
        newstring = newstring + " "
        

elif (tofrom == "from"):
    while len(instring) > 0:
        possible = "QWERTYUIOPASDFGHJKLZXCVBNM@.,?:/-='()_!&;$1234567890+ "
        possible = possible + '"'
    
print()
print()
print()
print(newstring)
print()
print()
print()
tofrom = input("Press enter to exit")
























