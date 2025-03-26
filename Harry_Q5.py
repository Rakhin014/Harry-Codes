import random
def Game():
    print("\t    Welcome to the Snake Water Gun game.")
    print("\tYou can choose between Snake Water and Gun")
    game = {1: "🐍", 2: "🌊" , 3: "🔫"}
    print("\t     Your options are 1.🐍. 2.🌊 3.🔫")
    uc = int(input("\t    Enter your choice "))
    while uc != 1 and uc != 2 and uc != 3 :
            print("The element you entered is invalid.\nPlease enter between 1,2,3")
            uc = int(input())
    print("\t    You have chosen", game[uc])
    pc = random.choice(list(game.keys()))
    print("\t    Computer has chosen ",game[pc])
    if uc == pc:
        print("It's a draw")
        print("Do you want to play again?")
        print("1. Yes  2. No")
        wish = int(input("Please enter your answer: "))
        while wish != 1 and wish != 2 :
            print("The element you entered is invalid.\nPlease enter between 1 and 2")
            wish = int(input())
        if wish == 1:
            Game()
        if wish == 2:
            print("OK sir, thank you for playing")
    elif uc == 1 and pc == 2:
        print("Your 🐍 has drunk the 🌊. You Won.")
        print("Do you want to play again?")
        print("1. Yes  2. No")
        wish = int(input("Please enter your answer: "))
        while wish != 1 and wish != 2 :
            print("The element you entered is invalid.\nPlease enter between 1 and 2")
            wish = int(input())
        if wish == 1:
            Game()
        if wish == 2:
            print("OK sir, thank you for playing")
    elif uc == 2 and pc == 1:
        print("Computer's 🐍 has drunk the 🌊. You Lost.")
        print("Do you want to play again?")
        print("1. Yes  2. No")
        wish = int(input("Please enter your answer: "))
        while wish != 1 and wish != 2 :
            print("The element you entered is invalid.\nPlease enter between 1 and 2")
            wish = int(input())
        if wish == 1:
            Game()
        if wish == 2:
            print("OK sir, thank you for playing")
    elif uc == 2 and pc == 3:
        print("Computer's 🔫 has drowned in 🌊. You Won.")
        print("Do you want to play again?")
        print("1. Yes  2. No")
        wish = int(input("Please enter your answer: "))
        while wish != 1 and wish != 2 :
            print("The element you entered is invalid.\nPlease enter between 1 and 2")
            wish = int(input())
        if wish == 1:
            Game()
        if wish == 2:
            print("OK sir, thank you for playing")
    elif uc == 3 and pc == 2:
        print("Your 🔫 has drowned in 🌊. You Lost.")
        print("Do you want to play again?")
        print("1. Yes  2. No")
        wish = int(input("Please enter your answer: "))
        while wish != 1 and wish != 2 :
            print("The element you entered is invalid.\nPlease enter between 1 and 2")
            wish = int(input())
        if wish == 1:
            Game()
        if wish == 2:
            print("OK sir, thank you for playing")
    elif uc == 1 and pc == 3:
        print("Computer's 🔫 have killed the 🐍. You Lost.")
        print("Do you want to play again?")
        print("1. Yes  2. No")
        wish = int(input("Please enter your answer: "))
        while wish != 1 and wish != 2 :
            print("The element you entered is invalid.\nPlease enter between 1 and 2")
            wish = int(input())
        if wish == 1:
            Game()
        if wish == 2:
            print("OK sir, thank you for playing")
    elif uc == 3 and pc == 1:
        print("Your 🔫 have killed the 🐍. You Won.")
        print("Do you want to play again?")
        print("1. Yes  2. No")
        wish = int(input("Please enter your answer: "))
        while wish != 1 and wish != 2 :
            print("The element you entered is invalid.\nPlease enter between 1 and 2")
            wish = int(input())
        if wish == 1:
            Game()
        if wish == 2:
            print("OK sir, thank you for playing")
Game()