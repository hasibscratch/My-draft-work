from datetime import datetime

# Function to calculate age
def calculate_age(birthdate):
    today = datetime.today()               # Get today's date
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Prompt user to enter birthdate
try:
    birth_date_input = input("Enter your birthdate (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")  # Convert input to date format
    age = calculate_age(birth_date)
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
