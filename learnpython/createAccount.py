# Create Account Function
def createaccount():
    while True:
        username = input("Create account, enter your username: ")
        password = input("Enter password: ")

        # Check if the password contains at least one letter and one digit
        if any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
            print("Account created successfully!")
            return username, password
        else:
            print("The created password is weak. Please include both letters and digits.")

# Login Function
def logIn(stored_username, stored_password):
    username1 = input("Login, enter your username: ")
    password1 = input("Enter your password: ")

    # Check if credentials match
    if username1 == stored_username and password1 == stored_password:
        print("Login is successful!")
    else:
        print("The credentials are wrong, please try again")

# Create an account and store the credentials
username, password = createaccount()

# Attempt to log in using the stored credentials
logIn(username, password)
