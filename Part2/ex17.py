import random

# Step 1: Ask user their name
name = input("Welcome agent. What's your real name? ")

# Step 2–4: Lists of adjectives and animals
adjectives = ['Sneaky', 'Invisible', 'Silent', 'Witty', 'Brave', 'Cunning']
animals = ['Otter', 'Panther', 'Falcon', 'Fox', 'Tiger', 'Chameleon']

# Step 5: Generate codename
codename = random.choice(adjectives) + " " + random.choice(animals)

# Step 6: Generate lucky number
lucky_number = random.randint(1, 99)

# Step 7: Print the final message
print(f"\nAgent {name}, your codename is **{codename}**.")
print(f"Your lucky number for this mission is: {lucky_number}")

