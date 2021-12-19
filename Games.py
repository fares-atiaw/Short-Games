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
        print(
            f'*** *** ***\nThis game is about *Multiplication Table*\nChoose a number to start and other to end with\n When you wanna exit, just print (q)\n')
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
                    print(f'The second number should be bigger than the first number you entered\nAgain !')
                    continue

                print()
                for x in range(x, y + 1):
                    for i in range(1, 11):
                        print(f' {x} X {i} = {x * i}')
                    print('------------')
                print('------------')
            except Exception as errormessage:
                print(f'Error : {errormessage}\n Please enter a valid number\n')



