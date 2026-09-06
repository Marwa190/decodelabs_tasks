import string

password = input("Enter your password: ")
score = 0

if len(password) >= 8:
    score += 1

if any(char .isupper( ) for char in password):
    score += 1

if any(char .isdigit( ) for char in password):
    score += 1

if any(char in string.punctuation
        for char in password):
    score +=1

if score <=1:
    strength = "Weak"

elif score<=3:
    strength = "Medium"

else:
    strength = "Strong"

print("Password Strength:",strength)