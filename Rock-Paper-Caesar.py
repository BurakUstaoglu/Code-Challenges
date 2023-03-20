import random

bRPC = ['rock', 'paper', 'scissors']
#bInput = str(input('Ready! Player One. Please choose your weapon >')) #>>>> int to str!!!!
#print(len(bRPC))
bScoreArray = [0, 50, 100]
bScore = int()

#region -----Stage 1/5
# if bInput != '' :
#     if bInput in bRPC:
#         x = bRPC[(bRPC.index(bInput) + 1) % len(bRPC)]
#         print('Sorry, but - I - the computer chose ' + x)

#     else:
#         print('Please be sure of your choice to be defeated')
#endregion

#region -----Stage 2/5
# if bInput != '':
#     if bInput in bRPC:
#         x = random.randrange(len(bRPC) - 1)
#         if (bRPC.index(bInput)+1) % len(bRPC) == x:
#             print("Sorry, you lose, the computer chose {}".format(bRPC[x]))

#         elif bRPC.index(bInput)-1 == x:
#             print("Well done. The computer chose {} and failed".format(bRPC[x]))

#         else:
#             print("There is a draw {}".format(bRPC[x]))
    
#     else:
#         print('Please be sure of your choice to be defeated')
#endregion

#region -----Stage 3/5
# while True:
#     bInput = str(input('Please choose your weapon >'))
#     if bInput != '':
#         if bInput in bRPC:
#             x = random.randrange(len(bRPC) - 1)

#             if (bRPC.index(bInput)+1) % len(bRPC) == x:
#                 print("Sorry, you lose, the computer chose {}".format(bRPC[x]))

#             elif bRPC.index(bInput)-1 == x:
#                 print("Well done. The computer chose {} and failed".format(bRPC[x]))

#             else:
#                 print("There is a draw {}".format(bRPC[x]))
#             continue

#         elif bInput == '!exit':
#             print('Bye!')
#             break

#         else:
#             print('Please be sure of your choice to be defeated')
#             continue
#endregion

#region -----Stage 4/5
# def FileManager(input):
#     f =  open("C:/Users/Maritime/Documents/GitHub/Challenges/ratings.txt", "r")
#     data = f.readlines()
#     for i in data:
#         bt = i.strip().split()
#         if input in bt:
#             global bScore
#             bScore = bt[1]
#             break
#     #print(bt)
#     f.close()

# def ScoreManager(bResult):
#     global bScore
#     bScore += bScoreArray[bResult]
#     # match bResult:
#     #     case -1:
#     #         bScore 
#     #         print()
        
#     #     case 0:
#     #         print()

#     #     case 1:
#     #         print()

# def GameManager():
#     bNameInput = str(input('Enter your name:'))
#     print('Hello ' + bNameInput)
#     FileManager(bNameInput)
#     while True:
#         bInput = str(input('Please choose your weapon >'))
#         if bInput != '':
#             if bInput in bRPC:
#                 x = random.randrange(len(bRPC) - 1)

#                 if (bRPC.index(bInput)+1) % len(bRPC) == x:
#                     ScoreManager(0)
#                     print("Sorry, you lose, the computer chose {}".format(bRPC[x]))

#                 elif bRPC.index(bInput)-1 == x:
#                     ScoreManager(2)
#                     print("Well done. The computer chose {} and failed".format(bRPC[x]))

#                 else:
#                     ScoreManager(1)
#                     print("There is a draw {}".format(bRPC[x]))
#                 continue

#             elif bInput == '!exit':
#                 print('Bye!')
#                 break
            
#             elif bInput == '!rating':
#                 print('Your rating: ' + str(bScore))

#             else:
#                 print('Please be sure of your choice to be defeated')
#                 continue

# GameManager()
#endregion

#region -----Stage 5/5
def FileManager(input):
    f =  open("C:/Users/Maritime/Documents/GitHub/Challenges/ratings.txt", "r")
    data = f.readlines()

    for i in data:
        bt = i.strip().split()

        if input in bt:
            global bScore
            bScore = int(bt[1])
            break

    f.close()

def ScoreManager(bResult):
    global bScore
    bScore += bScoreArray[bResult]

def GameMechanic():
    while True:
        bInput = str(input('Please choose your weapon >'))

        if bInput != '':
            if bInput in bRPC:
                x = random.randrange(len(bRPC))
                bResult = []
                for i in range(len(bRPC) // 2):
                    bResult.append((bRPC.index(bInput) + (i + 1)) % len(bRPC) )
                    #print(bResult)

                if x in bResult:
                    ScoreManager(0)
                    print("Sorry, you lose, the computer chose {}".format(bRPC[x]))

                elif x == bRPC.index(bInput):
                    ScoreManager(1)
                    print("There is a draw {}".format(bRPC[x]))

                else:
                    ScoreManager(2)
                    print("Well done. The computer chose {} and failed".format(bRPC[x]))
                continue

            elif bInput == '!exit':
                print('Your score: ' + str(bScore) + '\nBye!')
                break
            
            elif bInput == '!rating':
                print('Your score: ' + str(bScore))

            else:
                print('Please be sure of your choice to be defeated')
                continue

def GameManager():
    bNameInput = str(input('Enter your name:'))
    print('Hello ' + bNameInput)
    FileManager(bNameInput)

    global bRPC
    bOptionsInput = input("Please enter your options: ")
    if bOptionsInput != '':
        bRPC = bOptionsInput.split(',')

    if len(bRPC) % 2 == 1 and len(bRPC) > 1:
        print("Okay, let's start!")
        GameMechanic()
    else:
        print('Sum of your options must be an odd number.')

GameManager()
#endregion
