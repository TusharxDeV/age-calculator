from datetime import datetime

print("👋 Hello! Let's find out your age.")
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = datetime.now().year
age = current_year - birth_year

print(f"\nHi {name}, you are {age} years old in {current_year}!")
