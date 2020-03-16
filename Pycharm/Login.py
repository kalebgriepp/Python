print('Welcome to my secret program!')
time = 0

while True:
    username_actual = str('python')
    password_actual = str('csci135')

    username_trial = str(input('Please enter your username: '))
    if username_trial == username_actual:
        password_trial = str(input("Please enter your password: "))
        if password_trial == password_actual:
            print("Thanks for entering the correct username and password! \n I hope you have a GREAT day!!")
            exit()
        else:
            print("Invalid password")
    else:
        print("Invalid username")
    if time == 2:
        print("Too many attempts! You are locked out!")
        exit()
    time = time + 1
