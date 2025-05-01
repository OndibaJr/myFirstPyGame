print('WELCOME TO ADVENTURE GAME!!');  # Welcome message for the game

#getting user name and age
name=input('What is your name?:-) ');  # Prompt user for their name
age=int(input('What is your age?:-) '));  # Prompt user for their age and convert it to an integer

#out out the entered details
print('Hello', name, 'you are', age, 'years old!');  # Display the user's name and age

if age >= 18:  # Check if the user is old enough to play
    #User is old enough to play
    print('Yaaay!You are old enough to play!!');  # Inform the user they can play
    #Asking if the user wants to play
    wantsToPlay=input("Wanna play a game?? Yeah(Y) or Nope(N)? " );  # Ask if the user wants to play
    if wantsToPlay =='Y':  # If the user wants to play
        print("Let's GOOOOO!");  # Start the game

        #Game on!
        #Asking the user to choose a path
        directionChoice=input('What side are you going? Left(L) or Right(R): ');  # Ask the user to choose a direction
        if directionChoice=='L':  # If the user chooses Left
            print("Here, there is nothing Right! You're dead! GAMEOVER!!");  # Game over message for Left choice
        elif directionChoice=='R':  # If the user chooses Right
            print("You went right!You've reached a hill!! ");  # Inform the user they reached a hill
            hillMove=int(input("Go over it(1),Go through it by the troll caves(2): "));  # Ask how they want to proceed
            if hillMove==1:  # If the user chooses to go over the hill
                print("You have reached a lake!");  # Inform the user they reached a lake
                lakeMove=input("Swim across(A), Walk around it(Z): ");  # Ask how they want to cross the lake
                if lakeMove=='A':  # If the user chooses to swim across
                    print("A Gator finds you, guts you and.....Game Over!!");  # Game over message for swimming
                elif lakeMove=='Z':  # If the user chooses to walk around
                    print("You reached safely on the other side! You won!!");  # Winning message
                else:  # If the user enters an invalid input
                    print("Wrong input, we enda uza uji!!");  # Error message for invalid input
            elif hillMove==2:  # If the user chooses to go through the troll caves
                print("You found a hill troll!! You're dead!:-(");  # Game over message for troll encounter
            else:  # If the user enters an invalid input
                print("You have entered a wrong input! Run the code once again! Learn to follow directions bruh!");  # Error message for invalid input

        else:  # If the user enters an invalid direction
            print("Invalid choice! GAME OVER!!");  # Game over message for invalid direction
    #doesn't want to play
    elif wantsToPlay == 'N':  # If the user doesn't want to play
        print('Enda home!');  # Message for not playing
    else:  # If the user enters an invalid input
        print('Invalid input, run code again!!');  # Error message for invalid input
#Not old enough to play
else:  # If the user is not old enough to play
    print('Sorry buddy!You are not old enough to play:-(!');  # Message for underage users