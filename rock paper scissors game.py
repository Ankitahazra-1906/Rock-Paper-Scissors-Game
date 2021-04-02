import random
while True:
    user_choice=input("Enter any of the 3 choices between( rock ,paper and scissors): ")
    possible_choices=["rock","paper","scissors"]
    comp_choice=random.choice(possible_choices)
    print("\n You choose", user_choice ,"\n Comp choose", comp_choice,"\n")
    if user_choice==comp_choice:
        print("Its a tie!Both of you have chose", user_choice)
    elif user_choice=="rock":
        if comp_choice=="paper":
            print("You loose!Paper covers Rock")
        else:
            print("You win!Rock smashes Scissors")
    elif user_choice=="paper":
        if comp_choice=="scissors":
            print("You loose!Scissors cut the paper")
        else:
                print("You win!Paper covers Rock")
    elif user_choice=="scissors":
        if comp_choice=="rock":
            print("You loose!Rock smashes scissors")
        else:
            print("You win!Scissors cut the paper")
    continue_game=input("Do you want to continue the game(yes/no): ")
    if continue_game!="yes":
        break
    