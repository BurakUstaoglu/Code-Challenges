import random

bInput = str(input("Type uppercase, lowercase, number and total size of password with a space per input:"))
bSplittedT = [eval(x) for x in bInput.split(" ")]

bArrAllChars = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '0123456789']
bLastChecker = None

bPassword = str()

if bInput != '':
    if sum(bSplittedT[:-1]) <= bSplittedT[-1]:
        j = 0
        x = len(bArrAllChars[j])

        while(len(bPassword) < bSplittedT[-1]):
            bLenContainer = sum(bSplittedT[ : j + 1 ]) - len(bPassword)
            #print(bLenContainer)
            bLast = random.randrange(len(bArrAllChars [ j % len(bArrAllChars) ]) - 1)

            if bLast != bLastChecker and bLenContainer > 0 :
                bLastChecker = bLast
                bPassword += bArrAllChars[ j % len(bArrAllChars)][bLast]
                #print(bPassword)
                continue 

            elif bLenContainer <= 0 :
                j += 1
                #print('Here') 
                continue
            
            else:
                #j += 1
                continue
            
        print("It's dangerous to go alone! Take this: " + bPassword)

    else:
        print('Total size cannot be less than sum of the other 3 inputs')

else:
    print('Ah! In the end, you are always left with that same feeling: Emptiness')