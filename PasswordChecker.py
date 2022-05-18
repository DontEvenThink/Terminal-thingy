import time
import sys


def passwordcheck(password):
    """
    The passwordcheck function checks the password that is entered by the user and returns a permission level.
    The function checks if the password matches any of three predefined passwords, returning a corresponding
    permission level. If no match is found, it returns False.

    :param password: Used to store the password entered by the user.
    :return: The permissionlevel.
    """
    global permissionlevel
    permissionlevel = ""
    passadmin = "W3lc0met01h3h0M3L4nD"
    pass1 = "iloveb0afts"
    pass2 = "bean0s13supreme"
    if password == passadmin:
        permissionlevel = 0
        return permissionlevel
    elif password == pass1:
        permissionlevel = 1
        return permissionlevel
    elif password == pass2:
        permissionlevel = 2
        return permissionlevel
    else:
        permissionlevel = False
        return permissionlevel


passwordcheck(input("Enter your password here"))


if permissionlevel == 0:
    print("Password is correct!")
    time.sleep(2)
    username = input("What is your name?")
    time.sleep(0.6)
    print("Hello, Administrator " + username)
    time.sleep(0.6)
    print("Acessing terminal...")
    import Terminal.py
elif permissionlevel == 1:
    print("Password is correct!")
    time.sleep(2)
    print("Welcome, RaftLover456")
    time.sleep(0.6)
    print("Acessing terminal...")
    import Terminal.py
elif permissionlevel == 2:
    print("Password is correct!")
    time.sleep(2)
    print("Welcome, beanosdude")
    time.sleep(0.6)
    print("Acessing terminal...")
    import Terminal.py
elif permissionlevel == False:
    print("Password is incorrect!")
    print("Please restart the program and try again.")
    sys.exit()

else:
    print(
        "If you've got to this screen, you probably messed with the code or you input a value to break the code branch"
    )
    time.sleep(0.6)
    print(
        "Either way, you're going to have to fix the code manually (or if you just entered a wrong value, restart the program.)"
    )
