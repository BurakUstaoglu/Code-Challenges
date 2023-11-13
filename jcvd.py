bText = input("Do NOT type 'Hello World!':")
bBin = str()
bLastDigit = str()
bLocked = str()
bEncode = [' 00 0', ' 0 0']

for i in range(len(bText)):
    perChar =  str(bin(ord(bText[i])))[2:]
    #print(perChar)
    bBin += perChar

#print(bBin)

for i in range(len(bBin)):
    if bBin[i] != bLastDigit:
        bLastDigit = bBin[i]
        #print(bLastChar)
        bLocked += bEncode[int(bLastDigit)]
    else:
        bLocked += '0'
print(bLocked[1:])
