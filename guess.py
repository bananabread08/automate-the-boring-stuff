import random
print('Hello. What is your name?')
name = input()
print('Hello, ' + name + '!' + ' I am think of a number between 1 to 20.')

secret_number = random.randint(1,20)

for guesses in range(1,7):
    print('Take a guess')
    guess = input()
    if int(guess) == secret_number:
        break
    elif int(guess) < secret_number:
        print('Wrong. Higher please.')
    else:
        print('Wrong. Lower please.')

if guess == secret_number: 
    print('You guessed ' + str(secret_number) + '. You took ' + str(guesses) + ' guesses.')
else:
    print('Game over. The secret number is ' + str(secret_number))
