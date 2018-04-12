from Connection.userController import *
from Function.function import *
from AI.recognition import Recognition


option = {
    1:read_user,
    2:insert_user,
    3:update_user,
    4:delete_user,
    6:Recognition
    }

def switchCase(argument):
    func = option.get(argument,"invalid")
    return func()

choice = 0;
while True:
    menu()
    choice = int(input('Enter Your Choice : '))
    if choice > 0 and choice < 7:
        switchCase(choice)
    elif(str(choice)==str(10)):
        print("Thank You")
        break
    else:
        print("Wrong Input")
    input()
