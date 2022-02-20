game_list=[0,1,2]
def display(game_list):
    print("here is the list:")
    print(game_list)
def position_choice():
    choice='WRONG'
    while choice not in ['0','1','2']:
        choice=input("enter a number (0,1,2)\n")
        if choice not in ['0','1','2']:
             
             print("sorry please enter a number(0,1,2)")
    return (int(choice))
def replacement(game_list,position):
    name=input("enter what you want\n")
    game_list[position]=name
    return (game_list)
def play_choice():
        choice='WRONG'
        while choice not in ['Y','N']:
             choice=input("enter Y,N if you want to continue the game)\n")
             if choice not in ['Y','N']:
                 
                 print("PLEASE TELL YOU WANT TO PLAY OR NOT")
        if choice=='Y':
            return (True)
        else:
            return (False)
game_on=True
game_list=[0,1,2]
while game_on:
    display(game_list)
    position=position_choice()
    game_list=replacement(game_list,position)
    display(game_list)
    game_on=play_choice()




'''def user_choice():
    while True:
        choice=input("Enter a number between(0-10)\n")
        if choice.isdigit():
            if (int (choice)) in range(0,10):
             print (int(choice))
            else:
             print("please enter a number within range(0-10)")
        else:
            print("please enter a number")
user_choice()'''