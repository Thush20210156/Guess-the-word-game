secret='westminster'
turns=11
guesses=' '
missed=0
print(f'Let\'s play Guess the word \nYou have {turns} turns to guess the word!\
\n{" _ "*len(secret)}')

while turns>0:
    guess=str(input('Enter a guessed letter: '))
    guess=guess.lower()
    guesses+=guess#string concatenation step
   


    for letter in secret:
              if letter in guesses:
               print(' ',letter,' ',end=' ')
              else:
                  print(' _ ',end=' ')
                  missed+=1
    print()

    if missed==0:
        print('You win !')
        break
    if guess not in secret:
        turns-=1
        print('Incorrect')
        print(turns,'more turns')
    if turns==0:
        print('The answer is',secret)
print('End of Game')
 
