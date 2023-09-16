import random

def check_win(user, comp):
    if user == comp:
        return "It's a tie"
    elif user == "rock":
        if comp == "scissor":
            return "You Win"
        else:
            return "You Loss"
    elif user == "scissor":
        if comp == "paper":
            return "You Win"
        else:
            return "You Loss"
    elif user == "paper":
        if comp == "rock":
            return "You Win"
        else:
            return "You Loss"

user_input = input("Please choose from (rock,paper,scissor) : ")
options = ["rock", "paper", "scissor"]
comp_input = options[random.randint(0,2)]
print(f"User Input : {user_input}")
print(f"Computer Input : {comp_input}")
result = check_win(user_input, comp_input)
print(result)