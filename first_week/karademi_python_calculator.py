while(1):
    
    print(" 1 - / \n 2 - ^ \n 3 - + \n 4 - - \n 5 - * \n")
    operand = int(input("select an operand by character:\n"))
    if operand < 1 or operand > 5:
        operand = int(input("select an operand by character:\n"))
    first_num  = int(input("enter your first number(you can choose number less than 2,147,483,647 or greater than -2,147,483,648)\n"))
    if first_num >= 2147483647 or first_num <= -2147483648 :
        first_num  = int(input("is out of range ! please enter your first number again\n"))
 

    second_num  = int(input("enter your second number(you can choose number less than 2,147,483,647 or greater than -2,147,483,648)\n"))
    if second_num >= 2147483647 or second_num <= -2147483648 :
        second_num  = int(input("is out of range ! please enter your second number again\n"))


    if operand == 1 :
        try:
            result = first_num/second_num
            print(result)
            print("\n")
            print("\n")


        except ZeroDivisionError:

            print("cannot divide by zero\n")
            first_num  = int(input("enter your first number\n"))
            second_num  = int(input("enter your second number\n"))
    
    elif operand == 2 :
        result = first_num ** second_num
        if result >= 2147483647 or result <= -2147483648 :
             print("you should try again! this result is out of range!")
             first_num  = int(input("enter your first number\n"))
             second_num  = int(input("enter your second number\n"))
        else:
            print(result)
            print("\n")
            print("\n")

    
    elif operand == 3 :
        result = first_num + second_num
        if result >= 2147483647 or result <= -2147483648 :
             print("you should try again! this result is out of range!")
             first_num  = int(input("enter your first number\n"))
             second_num  = int(input("enter your second number\n"))
        else:
            print(result)
            print("\n")
            print("\n")

    
    elif operand == 4 :
        result = first_num - second_num
        if result >= 2147483647 or result <= -2147483648 :
             print("you should try again! this result is out of range!")
             first_num  = int(input("enter your first number\n"))
             second_num  = int(input("enter your second number\n"))
        else:
            print(result)
            print("\n")
            print("\n")


    elif operand == 5:
        result = first_num * second_num
        if result >= 2147483647 or result <= -2147483648 :
             print("you should try again! this result is out of range!")
             first_num  = int(input("enter your first number\n"))
             second_num  = int(input("enter your second number\n"))
        else:
            print(result)
            print("\n")
            print("\n")

