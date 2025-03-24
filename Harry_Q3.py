# Display question
# display options
# taking an answer as input
# varify the answer if it's right or wrong
# Add amount if the amount is right
# End the game if the answer is wrong and show the total amount.
print("Welcome to the game")
print("Here is your First Question")
Question = ["Question 1: What is your name?",
            "Question 2: What is your age?",
            "Question 3: What is your passion?"]
Answer = ["A. Afifa  B. Ayan  C. Araf  D. Yean",
          "A. 10  B. 12  C. 13  D. 15",
          "A. Teacher  B. Pilot  C. Doctor  D.Engineering"]
CA = ["B", "D", "D"]
i = 0
X = 0
def ques(i):
    global X
    if i>=len(Question):
        print("Game over")
        return
    print(Question[i])
    print(Answer[i])
    ans = input()
    while ans != "A" and ans != "B" and ans != "C" and ans != "D":
        print("The answer you have given is invalid\nPlease enter a character between A,B,C,D")
        ans = input()
    if ans == CA[i]:
        print("The answer is correct")
        if i==0:
            X = X+1000
            print("You have won", X , "TAKA.")
        else:
            X = X+2000
            print("You have won", X, "TAKA.")
        i = i+1
        ques(i)
    else :
        print("The answer is incorrect")
        print("You have won", X, "TAKA.")
ques(i)
