# It is a python program where the computer will take a number from 1 to 100 and you have to guess that number
# Now let's start the game
while True:
    import random
    print("Welcome to the game.")
    c = random.randint(1,100)
    u = int(input("Please enter a number that you have guessed "))
    while u != c:
        if u < c:
            print("Your number is lower than the computer")
            u = int(input("Please enter a number that you have guessed "))
        elif u > c:
             print("Your number is higher than the computer")
             u = int(input("Please enter a number that you have guessed "))
    print("Your answer is correct")
    print("Do you want to play again")
    print("1.Yes 2.No")
    a = int(input("Enter your answer "))
    while a != 1 and a != 2 :
        a = int(input("Enter your answer "))
    if a == 1:
        continue
    else:
        print("Thanks for playing")
        break
 