import random


game = {"rock": 0,
        "paper": 0,
        "scissor": 0}

keys = ("rock", "paper", "scissor")

counter = 0

wins = {
        "user":0,
        "Ai": 0,
        "Draw": 0
}

win_condition ={
        "rock": "paper",
        "paper": "scissor",
        "scissor": "rock"
}

def cheat_ai(user_choice):
        if user_choice == "rock":
                return win_condition["rock"]
        elif user_choice == "paper":
                return win_condition["paper"]
        elif user_choice == "scissor":
                return win_condition["scissor"]

def aichoice():
        global counter
        rock = game.get("rock", 0)
        paper = game.get("paper", 0)
        scissor = game.get("scissor", 0)
        move_counts = {"rock": rock, "paper": paper, "scissor": scissor}
        if counter >= 4:
                most_common_move = max(move_counts, key=move_counts.get)
                return win_condition[most_common_move]
        else:
                return random.choice(keys)

def gameplay(user_choice, Ai_choice):
        if user_choice == "rock" and Ai_choice == "paper":
                print("user lost and Ai wins")
                game[user_choice] = game.get(user_choice,0)+1
                wins["Ai"]+=1
        elif user_choice == "rock" and Ai_choice == "scissor":
                print("user wins and Ai Lost")
                game[user_choice] = game.get(user_choice,0)+1
                wins["user"]+=1
        elif user_choice == "paper" and Ai_choice == "rock":
                print("user wins and Ai lost")
                game[user_choice] = game.get(user_choice,0)+1
                wins["user"]+=1
        elif user_choice == "paper" and Ai_choice =="scissor":
                print("user lost and Ai wins")
                game[user_choice] = game.get(user_choice,0)+1
                wins["Ai"]+=1
        elif user_choice =="scissor" and Ai_choice == "rock":
                print("user Lost and Ai wins")
                game[user_choice] = game.get(user_choice,0)+1
                wins["Ai"]+=1
        elif user_choice == "scissor" and Ai_choice == "paper":
                print("user Wins and Ai Lost")
                wins["user"]+=1
                game[user_choice] = game.get(user_choice,0)+1
        elif user_choice == "paper" and Ai_choice == "paper":
                print("DRAW")
                game[user_choice] = game.get(user_choice,0)+1
                wins["Draw"]+=1
        elif user_choice == "scissor" and Ai_choice == "scissor":
                print("DRAW")
                game[user_choice] = game.get(user_choice,0)+1
                wins["Draw"]+=1
        elif user_choice == "rock" and Ai_choice == "rock":
                print("DRAW")
                game[user_choice] = game.get(user_choice,0)+1
                wins["Draw"]+=1


while True:

        print("""
        Welcome To ROCK, PAPER and SCISSOR (With AI)
        Choos the difficulty
        1.Easy(Tried to Learn machine learning concept with this but Failed Miserably)
        2.DEATH Mode(Sorry you have no chance If you choose this(Ofcourse this is more easy to bully you than making the Ai Learn))""")
        
        dificulty_choice = input("Choose anything 1 or 2: ")
        if dificulty_choice == "1":
                user_choice = input("Please choose rock, paper or scissor or q(quit): ")
                Ai_choice = aichoice()
                
                if user_choice == "rock" or user_choice == "paper" or user_choice == "scissor":
                        print(f"Your Choice: {user_choice}, AI Choice: {Ai_choice}")
                        gameplay(user_choice, Ai_choice)
                        counter +=1
                        print(game)
                elif user_choice == "q":
                        break
                else:
                        print("INVALID INPUT, please Choose rock, paper or scissor or q(quit)")
        elif dificulty_choice == "2":
                user_choice = input("Please choose rock, paper or scissor or q(quit): ")
                Ai_choice = cheat_ai(user_choice)
                
                if user_choice == "rock" or user_choice == "paper" or user_choice == "scissor":
                        print(f"Your Choice: {user_choice}, AI Choice: {Ai_choice}")
                        gameplay(user_choice, Ai_choice)
                        counter +=1
                        print(game)
                elif user_choice == "q":
                        break
                else:
                        print("INVALID INPUT, please Choose rock, paper or scissor or q(quit)")
