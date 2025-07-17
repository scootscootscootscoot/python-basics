'''our_number = 42

#get input

is_guessed = False

## while loop

while is_guessed == False:
 
    guess = int(input("enter your guess:"))


 ## if statement

    if guess == our_number:
        print('Hooray!')
        is_guessed = True
    elif guess > our_number:
        print('Too high!')
    else:
        print('Too low!')
        '''

counter = 1
while counter < 20:
 if counter % 3 == 0 and counter % 5 == 0:
    print(f'{counter}: Fizzbuzz')
 elif counter % 3 == 0:
    print(f'{counter}: Fizz')
 elif counter % 5 == 0:
    print(f'{counter}: Buzz')
 counter+= 1 # This is a shortcut for counter = counter + 1

else:
    print('Done with while loop')

