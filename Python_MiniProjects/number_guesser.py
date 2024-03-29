import random
# ^ this is a default python module, don't need to install

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0: 
        print('Please type a number larger than 0 next time') 
        quit()
else: 
    print ('Please type a number next time.') 
    quit()


random_number = random.randrange(top_of_range)
# this prints anything between 0 and the value of top_of_range
print(random_number)

guesses = 0

while True:
    # if you set this to true, you
    # have to use break keyword for it to not continue forever

    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
        # continue goes to next iteration

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else: 
        print("You were below the number")

print("You got it in", guesses, "guesses")
# the commas are automatically converted to a space " "
# the integer value stored in guesses is automatically converted to a string
# another way to write it: print("You got it in " + str(guesses) + " guesses")