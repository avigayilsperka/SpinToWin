import random

#instructions
print("\t\t\t\tSpin to Win!")
print()
print('Here\'s how to play:')
print('Can you beat the computor? For each of the 10 rounds, see who gets the higher roll \nof the dice.',end='')
print('The computor will keep track of the scores. All you have to do is spin!')
print()
print('\t\t\t\tGood Luck!')

uscore=0   #set accumulators to 0
cscore=0

play=1
while play==1:
    for x in range(10):   #loop 10 times    
        print('Round',x+1,':')  #title of round
        input('Click enter to roll')   
        uroll=random.randint(1,6)  #random int between 1 and 6
        croll=random.randint(1,6)
        print('You rolled a',uroll)
        print('The computor rolled a',croll)
        print()
        if uroll>croll:  #user wins
            print("You're the champ of the round!")
            uscore+=1
            
        elif uroll==croll:  #tie
            print('Tie!') 
        else:         #computor wins
                print('You lost, better luck next round!')
                cscore+=1
        print()
    #display grand winner    
    print("The grand winner is...")
    if uscore >cscore:
        print('You! Congratulations!')
    elif uscore == cscore:
        print("It's a tie! Play again for a final winner!")
    else:
        print('The computor! Great game!')

    print()
    play=0
    play=input('If you would like to play again, type 1 now!') #Allow user to play again

print('Thank you for playing!')


    
    
    
    
