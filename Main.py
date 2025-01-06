import random as rd
import time
import os

os.system("cls")

predefined=["Three years after the accepted answer clearly mentions",
            "The quick brown fox jumps over the lazy dog.",
            "I'm aiming at the flower! That's a fat guy in a flowered shirt.",
            "apple"
            ]

def typetest():
    prompt=rd.choice(predefined)
    stTime= time.time()

    os.system("cls")
    print(prompt)
    print("-------------------------------")
    inp= input()


    timeTaken=time.time()-stTime

    accuracy=0
    for i in range(0,len(prompt)):
        try:
            if prompt[i]== inp[i]:
                accuracy+=1
        except:
            break
    accuracy=int((accuracy/len(prompt)*100))

    wpm=int((len(inp)/5)/(timeTaken/60))

    print("-------------------------------")
    print("time taken "+str(timeTaken)[0:4]+"s")
    print("accuracy "+str(accuracy)+"%")
    print("Words per minuts "+str(wpm))
    print("-------------------------------")

run=True

while run:
    print("Type Test\n")
    print("1.Start")
    print("2.Exit")

    inp=input("action: ")
    match inp:
        case "1": typetest()
        case "2": run= False
        case _: 
            os.system("cls")
            print("Not an option")