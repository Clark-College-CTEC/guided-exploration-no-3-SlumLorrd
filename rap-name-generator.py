# Guided Exploration No. 3
# Matthew Aragon
# Import the random library becuase we will need it's functions.
import random
# Create an empty list. We will need to store stuff in it later.
possible_names = []
# This opens a new file so we can store the names that are generated.
outputFile = open('rap-names-output.txt', 'w')
# This opens the rap-names file and reads it, so we can do stuff with the file.
with open('rap-names.txt', 'r') as dataFile:
    # Use a loop to iterate through each line in rap-names.
    for name in dataFile:
        # Append the name in rap-names to the possible_names list.
        possible_names.append(name.rstrip())
# Ask the user to enter the number of rap names they want to create
# and store it in the count variable.
count = int(input('How many rap names would you like to create? '))
# Ask the user how many parts in the name and store it in the variable parts.
parts = int(input('How many parts should the name contain? '))
# Use a loop to generate the number of names the user wants to create.
for i in range(count):
    # Create an empty list to hold the rap names
    name_parts = []
    # This loop will iterate the number of times it was assigned to parts.
    for j in range(parts):
        # Each time the loop iterates it will select a name from the list
        # and append it to name_parts.
        # Random.randint will generate a random number from 0 to the length
        # of possible_names.
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
        # Use an f string to take the contents in name_parts and glue them
        # together with a space.
        outputFile.write(f"{' '.join(name_parts)}\n")
        # Use an f string to print out the final name generated.
        print(f"{' '.join(name_parts)}")

# This closes the output file.
outputFile.close()
