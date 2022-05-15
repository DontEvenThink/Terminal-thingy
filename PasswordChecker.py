import time
import sys

def passwordcheck(password):
    """
    The passwordcheck function checks if the password entered by a user matches the real password.
    If it does, then True is returned. If not, False is returned.
    
    :param password: Used to Store the password entered by the user.
    :return: The result variable.
    
    :doc-author: Ender and Trelent
    """
    
    realpassword = "W3lc0met01h3h0M3L4nD"
    if password == realpassword:
        result = True
        return result
    else:
        result = False
        return result
    
passwordcheck(input ("Enter your password here"))

global result


if result == True:
    print ("Password is correct!")
    time.sleep(2)
    username = input ("What is your name?")
    time.sleep(0.6)
    print ("Hello," + username)
    time.sleep(0.6)
    print ("Acessing terminal...")
    import Terminal.py
elif result != True:
    print ("Error, your password is incorrect.")
    time.sleep(0.6)
    print("Please restart the application and try again.")
    sys.exit()
else:
    print ("If you've got to this screen, you probably messed with the code or you input a value to break the code branch")
    time.sleep(0.6)
    print ("Either way, you're going to have to fix the code manually (or if you just entered a wrong value, restart the program.)")
    




