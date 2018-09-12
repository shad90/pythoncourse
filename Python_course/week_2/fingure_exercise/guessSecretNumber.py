#Week-2 Finger Exerices
#Guess Secret Number
#Implementation of Bisection Method
high = 100
low = 0
guess = (high+low)//2
print("Please think of a number between 0 and 100!")
while True:
    print ("Is your secret number " + str(guess) + "?")
    hlc = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if (hlc == 'h'):
        high = guess
        guess = (high+low)//2
    elif (hlc == 'l'):
        low = guess
        guess = (high+low)//2
    elif (hlc == 'c'):
        break
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was:",guess)
