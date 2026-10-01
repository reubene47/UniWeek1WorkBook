# # Ask user to enter their name
# print("What is your name?")
# name = input()
# print(f"It is nice to meet you {name}")

# eye_char = input("Please enter a character for the eye: ")

# print("##########")
# print(f"#| {eye_char}  {eye_char} |#")
# print("#| ---- |#")
# print("##########")

# name = input("What is your name?: ")
# age = input("How old are you (in years)?: ")

# height = input("How tall are you (in meters)?: ")
# weight = input("How much do you weigh (in kilograms)?: ")
# bmi = float(weight) / (float(height) ** 2)

# print(f"{name} you are {age} years old and your bmi is {bmi:.2f}")

lives = int(input("Please enter the number of lives: "))
energy = int(input("Please enter the energy level: "))
shield = int(input("Please enter the shield level: "))

print("Health has been set")
print(f"Lives: {"♥" * lives}")
print(f"Energy: {"♦" * energy}")
print(f"Shield: {"♦" * shield}")