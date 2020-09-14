import json

def get_stored_username():
    """Get stored username if available."""
    filename = '10/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = '10/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username=get_stored_username()
    if username:
        print('Are you '+username+' ?')
        temp=input('Y/N ')
        if temp =='N':
            username=get_new_username()
        elif temp == 'Y':
            print('Welcome Back! '+username)
    else:
        username=get_new_username()

greet_user()