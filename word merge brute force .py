import random
import itertools
#import sys

# Read the list of dictionary words from two files
with open('part1.txt', 'r') as f1, open('part2.txt', 'r') as f2:
    dictionary1 = [line.strip() for line in f1]
    dictionary2 = [line.strip() for line in f2]

# Choose a random word from each dictionary
word1 = random.choice(dictionary1)
word2 = random.choice(dictionary2)

# Capitalize a random letter in each word
capitalized_word1 = word1.capitalize()
index1 = random.randint(0, len(word1)-1)
capitalized_word1 = capitalized_word1[:index1] + capitalized_word1[index1].upper() + capitalized_word1[index1+1:]

capitalized_word2 = word2.capitalize()
index2 = random.randint(0, len(word2)-1)
capitalized_word2 = capitalized_word2[:index2] + capitalized_word2[index2].upper() + capitalized_word2[index2+1:]

# Merge the two words and add a random number to the end
password = capitalized_word1 + capitalized_word2 + str(random.randint(100, 999))

# Get the minimum and maximum password length from standard input
min_length = int(input("Enter the minimum password length: "))
max_length = int(input("Enter the maximum password length: "))

# Generate all permutations of the password with the given length range
perms = []
for length in range(min_length, max_length+1):
    for p in itertools.product(password, repeat=length):
        perm = ''.join(p)
        perms.append(perm)

# Save the permutations to a file
with open('password_perms.txt', 'w') as f:
    for perm in perms:
        f.write(perm + '\n')

print(f"{len(perms)} possible passwords generated and saved to 'password_perms.txt'.")
