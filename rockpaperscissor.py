import random
# 5 condition 1) computer wins 1>2 2>1 2)user wins 
# 1>2 2>1 3)draw 0=0 1=1 2=2 4) getting 0 or 2 either on computer side or by user 5)invalid input
print("ROCK PAPER SCISSOR GAME")
def play_game():
    rock = '''
        ___
    ---'   __)
         (_)
         (_) 
          ()
    ---.(_)
     '''
    paper = '''
       ___
    ---' )
             __)
            ___)
            ___)
    ---.)
    '''
    scissor = '''
      ___
      ---'   )
                __)
             ____)
            ()
      ---.(_)
     '''
    gameimages = [rock, paper, scissor]

    userscore = 0
    computerscore = 0
    roundnumber = 1

    while True:
        print(f"Round {roundnumber}")
        user_choice = int(input("Enter the number: type 0 for Rock, 1 for Paper, 2 for Scissor: "))
        if user_choice >= 3 or user_choice < 0:
            print("Invalid input")
        else:
            print("Your choice:")
            print(gameimages[user_choice])
            computer_choice = random.randint(0, 2)
            print(f"Computer choice ({computer_choice}):")
            print(gameimages[computer_choice])

            if computer_choice == user_choice:
                print("It's a draw")
            elif computer_choice == 0 and user_choice == 2:
                print("Rock smashes scissors! You lose")
                computerscore += 1
            elif computer_choice == 2 and user_choice == 0:
                print("Rock smashes scissors! You win")
                userscore += 1
            elif computer_choice > user_choice:
                print("You lose.")
                computerscore += 1
            elif user_choice > computer_choice:
                print("You win.")
                userscore += 1
        play_again = input("Wanna play another round (yes/no): ").lower()
        if play_again != 'yes':
            break

        roundnumber += 1

    print("Game Over")
    print(f"Final Score: Your Score!! {userscore} - Computer ^^ score  {computerscore}")
    print(f" TOTAL ROUND PLAYES {roundnumber}")
print("ROCK PAPER SCISSOR GAME")
play_game()