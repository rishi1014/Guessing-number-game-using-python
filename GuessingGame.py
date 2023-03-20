import random 

num = random.randint(1,100)

guessess = [0]

while True:
    guess = int(input("Guess a number between 1-100 : "))
    
    if guess <1 or guess>100 :
        print("Out of bounds !!  Number guess should be between 1-100 please try again :")
        continue 
    if guess == num:
        print(f"CONGRATULATION YOU GUESSED THE NUMBER , IN ONLY {len(guessess)} GUSSESS!!")
        break
    # if guess is incorrect 
    guessess.append(guess)
    
    if guessess[-2]:
        if abs(num-guess) < abs (num - guessess[-2]):
            print("WARMER")
        else:
            print("COLDER")
    else:
        if abs(num-guess) <=10 :
            print("warm")
        else:
            print("cold")