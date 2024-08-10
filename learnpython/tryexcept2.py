# try exceptional for the digit of number and valid email/gmail
def three_digit_num():
    while True:
        try:
            x = int(input("Please Enter the number of three digits: "))
            if 100<=x<=999:
                return x
            else:
                print("The number you entered is invalid, pls try agian ")
        except Exception as e:
            return e 
name = str(input("Write your Name: "))


mynumber = three_digit_num()

print(name, "your three digit number is ", mynumber)

def email_gmail():
    while True:
        try:
            email= input("Please enter valide email: ")
            if "@" and "." in email:
                return email
            else:
                print("please enter valid email that contains @ and . symbols")
        except Exception as e:
            return e


myemail= email_gmail()

print(f'Thank you for your information {name}, Your email is {myemail}')