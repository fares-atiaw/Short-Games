from Games import Game


def welcome_choice():
    print("Welcome!\n Choose which game you wanna play \n"
          "Press [1] => Even / Odd Game \n"
          "Press [2] => Sum & Average Game \n"
          "Press [3] => Multiplication Game \n"
          "Press [4] => Power numbers \n"
          "Press [5] => Where is my item ? \n"
          "Press [6] => I like Even numbers only ! \n"
          "Press [7] => I like Odd numbers only ! \n"
          " ... When you wanna quit, just write (123)\n")


def choices():
    while True:
        try:
            x = input("@()()()()()@\nEnter your choice : ")
            if x == '1':
                Game.Even_or_Odd_Game()
            elif x == '2':
                Game.Sum_Average_Game()
            elif x == '3':
                Game.Multiplication_Game()
            elif x == '4':
                Game.Power_Numbers()
            elif x == '5':
                Game.Where_is_my_item()
            elif x == '6':
                Game.Get_Even_Numbers()
            elif x == '7':
                Game.Get_Odd_Numbers()
            elif x == '123':
                print(f'We hope you have enjoyed. Salam !')
                break
            else:
                print(f'Choose (1) , (2) or (3) ... If you wanna quit, just write (123)\n')
        except Exception as e:
            print(e)


class Play:
    welcome_choice()
    choices()
