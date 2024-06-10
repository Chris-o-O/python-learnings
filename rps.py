import random

# we ask user to play rps and how many winning rouds
user_score = 0
cpu_score = 0

user_intent = input("do you want to play rock paper scissors: yes or no?")

if user_intent != "yes" and user_intent != "ok":
    quit()
else:
    print("great")

# computer chooses a value

plays = ["rock","paper","scissors"]

cpu_play = plays[random.randrange(0,len(plays))]


# alternative initialement prop
#plays = [{"play":"rock"},
#        {"play":"paper"},
#        {"play":"scissors"}]

#cpu_play = plays[random.randrange(0,len(plays))]["play"]

# user chooses a value

while True:
    try:
        user_play = input("type in your hand: rock, paper or scissors? ")
    except ValueError:
        pass
    else:
        break     

while True:
    #if user_play != "rock" and user_play != "paper" and user_play != "scissors":
    if user_play not in plays: 
        user_play = input("type in one of those options: rock, paper or scissors? ")
    else:
        break

# keep track of score

print("You played ", user_play, "and computer played ",cpu_play)

if user_play == cpu_play:
    print ("it's a tie")
    user_score += 0
    cpu_score += 0

elif user_play == "rock" and cpu_play == "scissors":
    print ("you win that round")
    user_score += 1
    cpu_score += 0

elif user_play == "paper" and cpu_play == "rock":
    print ("you win that round")
    user_score += 1
    cpu_score += 0

elif user_play == "scissors" and cpu_play == "paper":
    print ("you win this round")
    user_score += 1
    cpu_score += 0

else: 
    print ("you lose this round")
    user_score += 0
    cpu_score += 1

print (f" scores:\n you : {user_score}\n VS\n computer : {cpu_score}")

