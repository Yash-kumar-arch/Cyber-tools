
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
strength , suggestions = strength_checker(passwd) # func returns strength and suggestions in tuple format (strength,suggestions)
                    #result = strenght_checker(passwd) which is ["weak","It should have uppercase"] #so  strenght = result[0] suggestions = result[1]
print(f"\nStrength: {strength}")

if suggestions:   # checks 
    print("Suggestions:")
    for tip in suggestions:
        print(f"  - {tip}")

'''
1.tried to use if else rather than functions 
2.then tried to check return passwd.isalnum() which is wrong cause they check on all characters rather than one of the characters
3.Didnt know use of any func and generators 
4.Didnt thought of using list for suggestions 
5.Made silly mistakes like isdigit and not using brackets isdigit()
6.Wrote the remaining code below return forget that after return func ends there 

'''

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


'''
1.random.choice only takes one argument
2.string.ascii gives all char. a-z and string.digits 0-9
3.now characters store all possible combinations like char. = ABCDEFGHabcdefgh123456789!@#$%^&*
4.now loop iterate over every value in char. and choose randomly using random and add to password 

'''
    




