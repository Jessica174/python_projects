import random
score=0
num=0
n=random.randrange(1,20)
def main():
    n=random.randrange(1,20)
    global num
    global score
    Lives=3
    while Lives>=1:
        Guess_no=int(input("Enter any number:"))
        if n==Guess_no:
            print('\nGREAT!You guessed it right!!\n')
            if Lives==3:
                score +=25
            elif Lives==2:
                score +=15
            elif Lives==1:
                score +=5
            break
        elif n>=Guess_no:
            Lives -= 1
            print('\nTOO LOW\n')
            print('\nYou guessed incorrectly. Try Again',Lives,'Lives remaining.\n')
            if Lives==0:
                print("\nThe number was:",n,'!\n')

        elif n<=Guess_no:
            Lives -= 1
            print('\nTOO HIGH\n')
            print('\nYou guessed incorrectly. Try Again',Lives,'Lives remaining.\n')
            if Lives==0:
                print("\nThe number was:",n,'!\n')


def end():
    global score
    play_again=input('Would you like to play again?[yes/no]')
    while play_again.lower()=='yes':
        if play_again.lower()=='yes':
            n=random.randrange(1,20)
            main()
            play_again=input('Would you like to play again?[yes/no]')
            if play_again.lower()=='no':
                break
    if play_again.lower()=='no':
        print("Your Score is"+str(score))
        input('Ok,Press enter to exit the game')
        exit()
main()
end()            
