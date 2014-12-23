CS303
=====

projects 

def main():

# Prompt the user to enter a positive number
    n = int(input('Enter a positive number: '))
    while (n < 0):
     print ('Negative number. Try again.')
     n = int(input('Enter a positive number:'))
# Initialize oldGuess and newGuess
    oldGuess = n / 2.0
    newGuess = 0
# Write result
    difference = abs(newGuess-oldGuess)
    while (difference >= 1 * 10 ** -6):
     newGuess = ((n / oldGuess) + oldGuess) / 2.0
     difference = abs(newGuess - oldGuess)
     oldGuess = newGuess
    print ('Square Root is: ', newGuess)
# Compute difference your value and Python's value
    diff = newGuess - n ** 0.5
    print ('Difference is: ', diff)

main()
