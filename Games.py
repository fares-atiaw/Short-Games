class Game:

    def __init__(self):
        pass

    @staticmethod
    def Even_or_Odd_Game():
        print(f'*** *** ***\nThis game find out if the entered number is Even or Odd\n When you wanna exit, just print (q)\n')
        while True:
            try:
                x = input(f'Enter the number : ')
                if x == 'q':
                    break
                elif int(x) % 2 == 0:
                    print(f'{x} is an even number\n--------------\n')
                else:
                    print(f'{x} is an odd number\n--------------\n')
            except Exception as e:
                print("Wrong : ", e)

    @staticmethod
    def Sum_Average_Game():
        print(f'*** *** ***\nThis game is about taking average of the entered numbers\n When you wanna exit, just print (q)\n')
        while True:
            try:
                count = input(f'Enter how many numbers do you want : ')
                if count == 'q':
                    break
                print()
                i = 1
                sum_num = 0

                while i <= float(count):
                    try:
                        num = float(input(f'Enter number {i} : '))
                        sum_num += num
                        i += 1
                    except Exception as e:
                        print('Error: ', e)

                print(f'========\n  The sum of your numbers is : {sum_num}')
                print(f'  The average of your numbers is : {sum_num / float(count)}\n')
            except Exception as r:
                print('Error: ', r)

    @staticmethod
    def Multiplication_Game():
        print(f'*** *** ***\nThis game is about *Multiplication Table*\nChoose a number to start and other to end with\n When you wanna exit, just print (q)\n')
        while True:
            try:
                x = input(f'Enter the first number : ')
                if x == 'q':
                    print(f'We hope you have enjoyed. Salam !')
                    break
                x = int(x)
                y = input(f'Enter the second bigger number : ')
                if y == 'q':
                    break
                y = int(y)

                if y < x:
                    print(f'The second number should be bigger than the first number you entered\nAgain ! ')
                    continue

                print()
                for x in range(x, y + 1):
                    for i in range(1, 11):
                        print(f' {x} X {i} = {x * i}')
                    print('------------')
                print('------------')
            except Exception as errormessage:
                print(f'Error : {errormessage}\n Please enter a valid number\n')

    @staticmethod
    def Power_Numbers():     # Using List comprehensions
        print(
            f'*** *** ***\nThis game is about taking the first integer number and the second integer number\n and give all the numbers between them back *Powered*\n When you wanna exit, just print (q)\n')
        while True:
            try:
                start = input(f'Enter the first number : ')
                if start == 'q':
                    print(f'We hope you have enjoyed. Salam !')
                    break
                start = int(start)
                end = input(f'Enter the second bigger number : ')
                if end == 'q':
                    break
                end = int(end)

                if end < start:
                    print(f'The second number should be bigger than the first number you entered\nAgain ! ')
                    continue

                print()
                lista = [n for n in range(start, end + 1)]
                print(f'Your list => {lista}')
                lista = [n ** 2 for n in lista]
                print(f'\nYour powered list => {lista}\n')
            except Exception as e:
                print(e)

    @staticmethod
    def Where_is_my_item():     # Using List comprehensions
        print(
            f'*** *** ***\nThis game is about exploring the given item inside the given list -- Right now it works only on list of numbers --\n When you wanna exit, just print (q)\n')
        while True:
            try:
                item = input(f'Enter the item : ')
                if item == 'q':
                    break
                elif item == '':
                    print("Enter an item first \n")
                    continue
                l = input(f'Enter the list : ')
                if l == 'q':
                    break
                elif l is None:
                    print("Enter a list first \n")
                    continue

                print(f'\n{l}')
                lista = [item if w==item else 'X' for w in l]
                print(f'\nIndex: {lista.index(item)+1}/{len(lista)} => {lista}\n')
            except Exception as e:
                print(f'Wrong: ', f'{e}\n')

    @staticmethod
    def Get_Even_Numbers():     # Using List comprehensions
        print(
            f'*** *** ***\nThis game is about getting the +even numbers+ between the first integer number and the second integer number\n When you wanna exit, just print (q)\n')
        while True:
            try:
                start = input(f'Enter the first number : ')
                if start == 'q':
                    break
                start = int(start)

                end = input(f'Enter the second bigger number : ')
                if end == 'q':
                    break
                end = int(end)

                if end < start:
                    print(f'The second number should be bigger than the first number you entered\nAgain ! ')
                    continue

                show_odd = input(f'Enter any key if you want to replace the odd numbers with the word \'Odd\' : ')
                if show_odd == "":
                    lista =[n for n in range(start, end+1) if n % 2 == 0]
                else:
                    lista = [n if n % 2 == 0 else 'Odd' for n in range(start, end + 1)]

                print(f'\nYour Even list => {lista}\n')
            except Exception as e:
                print(e)

    @staticmethod
    def Get_Odd_Numbers():     # Using List comprehensions
        print(
            f'*** *** ***\nThis game is about getting the -odd numbers- between the first integer number and the second integer number\n When you wanna exit, just print (q)\n')
        while True:
            try:
                start = input(f'Enter the first number : ')
                if start == 'q':
                    break
                start = int(start)

                end = input(f'Enter the second bigger number : ')
                if end == 'q':
                    break
                end = int(end)

                if end < start:
                    print(f'The second number should be bigger than the first number you entered\nAgain ! ')
                    continue

                show_even = input(f'Enter any key if you want to replace the even numbers with the word \'Even\' : ')
                if show_even == "":
                    lista = [n for n in range(start, end + 1) if n % 2 != 0]
                else:
                    lista = [n if n % 2 != 0 else 'Even' for n in range(start, end + 1)]

                print(f'\nYour Odd list => {lista}\n')
            except Exception as e:
                print(e)




    # @staticmethod
    # def Where_is_my_item():     # Using List comprehensions
    #     print(
    # f'*** *** ***\nThis game is about exploring the given item inside the given list -- Right now it works only on list of numbers --\n When you wanna exit, just print (q)\n')
    #     while True:
    #         try:
    #             item = input(f'Enter the item : ')
    #             if item == 'q':
    #                 break
    #             l = input(f'Enter the list : ')
    #             if l == 'q':
    #                 break
    #
    #             print(f'\n{l}')
    #             lista = [item if w==item else 'X' for w in l]
    #             print(f'\nIndex: {lista.index(item)+1}/{len(lista)} => {lista}\n')
    #         except Exception as e:
    #             print(f'Wrong: ', f'{e}\n')
