import random as rd
import time
import os
from difflib import SequenceMatcher

os.system("cls")

#importing sentences
with open("senteces.txt", 'r') as file:
        lines = file.readlines()
        sentences= [line.strip() for line in lines]

# function to check accuracy of input
def StringAccuracy(str1, str2):
    similarity_ratio = SequenceMatcher(None, str1, str2).ratio()

    similarity_percentage = similarity_ratio * 100
    return round(similarity_percentage, 2)


# function of the test
def typetest():
    prompt=rd.choice(sentences)
    stTime= time.time()

    os.system("cls")
    print(prompt)
    print("-------------------------------")
    inp= input()


    timeTaken=time.time()-stTime

    accuracy= StringAccuracy(prompt,inp)

    wpm=int((len(inp)/5)/(timeTaken/60))

    print("-------------------------------")
    print("time taken "+str(timeTaken)[0:4]+"s")
    print("accuracy "+str(accuracy)+"%")
    print("Words per minuts "+str(wpm))
    print("-------------------------------")



#main loop for the program with simple menu
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
