from Games import Game


def welcome_choice():
    print("Welcome!\n Choose which game you wanna play \n"
          "Press [1] => Even / Odd Game \n"
          "Press [2] => Sum & Average Game \n"
          "Press [3] => Multiplication Game \n"
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
