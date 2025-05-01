print('WELCOME TO ADVENTURE GAME!!');

name=input('What is your name?:-) ');
age=int(input('What is your age?:-) '));


print('Hello', name, 'you are', age, 'years old!');

if age >= 18:
    print('Yaaay!You are old enough to play!!');
    #Old enough to play
    wantsToPlay=input("Wanna play a game?? Yeah(Y) or Nope(N)? " );
    if wantsToPlay =='Y':
        print("Let's GOOOOO!");

        #Game on!
        directionChoice=input('What side are you going? Left(L) or Right(R): ');
        if directionChoice=='L':
            print("Here, there is nothing Right! You're dead! GAMEOVER!!");
        elif directionChoice=='R':
            print("You went right!You've reached a hill!! ");
            hillMove=int(input("Go over it(1),Go through it by the troll caves(2): "));
            if hillMove==1:
                print("You have reached a lake!");
                lakeMove=input("Swim across(A), Walk around it(Z): ");
                if lakeMove=='A':
                    print("A Gator finds you, guts you and.....Game Over!!");
                elif lakeMove=='Z':
                    print("You reached safely on the other side! You won!!");
                else:
                    print("Wrong input, we enda uza uji!!");
            elif hillMove==2:
                print("You found a hill troll!! You're dead!:-(");
            else:
                print("You have entered a wrong input! Run the code once again! Learn to follow directions bruh!");

        else:
            print("Invalid choice! GAME OVER!!");
    #doesn't want to play
    elif wantsToPlay == 'N':
        print('Enda home!');
    else:
        print('Invalid input, run code again!!');
#Not old enough to play
else:
    print('Sorry buddy!You are not old enough to play:-(!');    



