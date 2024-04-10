import random


def answer1():
    print("Let's play rock paper scissors!")
    while True: 
        answer = input("rock, paper, or scissors?")
        answer1 = answer.lower()
        if answer1 in ["rock" , "paper" , "scissors"]:
            return answer1
        else:
            print("Please input an actual choice")

def computeranswer():
    randomanswer = ["rock" , "paper" , "scissors"]
    return random.choice(randomanswer)

def winner(answer1, computeranswer):   

    if answer1 == computeranswer:
        return "It's a tie!"

    elif (answer1 == "rock" and computeranswer == "scissors" or 
          answer1 == "paper" and computeranswer == "rock"    or
          answer1 == "scissors" and computeranswer == "paper" ):
        return "WOOHOO YOU WIN!"
    
    else: 
        return "Sorry, you lost!"


def main():

    youranswer = answer1()
    randomanswer = computeranswer()

    print(f"You chose {youranswer}")
    print(f"The computer chose {randomanswer}")
    print(winner(youranswer, randomanswer))

if __name__ == "__main__":
    main()
