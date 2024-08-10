# simple try except:
try:
    x = int(input('Enter your number: '))
    print('your number is', x)
except:
    print("The value you entered is not integer pls try... again")
 
# TypeError

def addnumbers(num1,num2, num3):

    try:
        return (num1+num2+num3) 
    except TypeError:
        return ("Python is not support to add the str type with int")
print(addnumbers(4,4,4))
print(addnumbers(5,5,5))
print(addnumbers(6,"a",6))
print(addnumbers(7,7,7))
print("The execuation is completed")


# But actual we don't know which errors to be happened so that we can use 
# try
# except Exception as e 
# return(e) let see below example 

def twonum(a,b): 
    try:
        return(a+b)
    except Exception as e:
        return(e)
print(twonum(4,4))
print(twonum(4,5))
print(twonum(4,"y"))
print('The execuation is completed')