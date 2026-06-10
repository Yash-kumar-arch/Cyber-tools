
def length(passwd):
    return len(passwd) >= 8 

def upper(passwd):
    return any(c.isupper() for c in passwd)

def lower(passwd):
    return any(c.islower() for c in passwd)

def digit(passwd):
   return any(c.isdigit() for c in passwd)

def special(passwd):
    return any(c in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for c in passwd)


def strength_checker(passwd):
    score = 0
    suggestions = []

    if length(passwd):
        score +=1
    else:
        suggestions.append("Password should be more than 8 characters")
    if upper(passwd):
        score += 1
    else:
        suggestions.append("It should have uppercase letters")
    
    if lower(passwd):
        score += 1
    else:
        suggestions.append("It should have lowercase letters")
    if digit(passwd):
        score += 1 
    else:
        suggestions.append("It should have digits")
    if special(passwd):
        score += 1
    else:
        suggestions.append("It should have special characters")
    
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    return strength , suggestions

passwd = input("Enter password: ")   
strength , suggestions = strength_checker(passwd) 

if suggestions:   # checks 
    print("Suggestions:")
    for tip in suggestions:
        print(f"  - {tip}")



import random 
import string

characters = string.ascii_uppercase+string.ascii_lowercase+string.digits+"!@#$%^&*()"

def generate_password(length):
    # guarantee one of each type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()")
    ]
    
    # fill remaining length with random characters
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*()"
    for i in range(length - 4):
        password.append(random.choice(characters))
    
    # shuffle so guaranteed characters aren't always at start
    random.shuffle(password)  # shuffles the list in place
    return ''.join(password)  # joins list into string and returns

generated = generate_password(12)
strength, suggestions = strength_checker(generated)
print("\nThe generated password is: ")
print(generated)
print(f"Strength: {strength}")


    




