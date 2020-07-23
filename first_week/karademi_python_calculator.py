def power_supply(first_num, second_num):
    power_result = first_num ** second_num
    return power_result


def summation(first_num, second_num):
    sum_result = first_num + second_num
    return sum_result


def submission(first_num, second_num):
    submission_result = first_num - second_num
    return submission_result


def multiplication(first_num, second_num):
    multiplication_result = first_num * second_num
    return multiplication_result


result = 0
operator = 0
while operator != 6:
    try:
        input_num = int(input("enter your number\n"))
    except ValueError:
        print("you should enter integer:")

    try:
        operator = int(
            input(
                "select an operator by number:\n"
                "1 - division \n "
                "2 - power  \n "
                "3 - summation \n "
                "4 - submission \n "
                "5 - multiplication \n "
                "6 - quit \n"
            )
        )
        if operator < 1 or operator > 6:
            print("you are wrong! please choose between 1 - 6")
            operator = int(
                input(
                    "select an operand by number:\n"
                    "1 - division \n "
                    "2 - power  \n "
                    "3 - summation \n "
                    "4 - submission \n "
                    "5 - multiplication \n "
                    "6 - quit \n"
                )
            )
    except ValueError:
        print("you should enter integer:")

    if operator == 1:
        try:
            previous_result = result
            result = result / input_num
            print(f"{previous_result} / {input_num} = {result}\n")

        except ZeroDivisionError:

            print("cannot divide by zero\n")

    elif operator == 2:
        previous_result = result
        result = power_supply(result, input_num)
        print(f"{previous_result} ^ {input_num} = {result}\n")

    elif operator == 3:
        previous_result = result
        result = summation(result, input_num)
        print(f"{previous_result} + {input_num} = {result}\n")

    elif operator == 4:
        previous_result = result
        result = submission(result, input_num)
        print(f"{previous_result} - {input_num} = {result}\n")

    elif operator == 5:
        previous_result = result
        result = multiplication(result, input_num)
        print(f"{previous_result} * {input_num} = {result}\n")

print("have a good time :)")
