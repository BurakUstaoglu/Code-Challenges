bText = input("Type your secrets:")
bSplittedT = []
bSplittedT = bText.split(" ")

binaryD = str()
bDecodedText = str()

for i in range(0, len(bSplittedT), 2):
    x = len(bSplittedT[i + 1])
    
    if bSplittedT[i] == '0' :
        binaryD += "1" * x

    elif bSplittedT[i] == '00' :
        binaryD += "0" * x

print(binaryD)
#-----CopyPasteArea-----