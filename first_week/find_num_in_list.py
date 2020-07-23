# in this program we enter the list of numbers
# then we enter number
# we find tow number in list that summation of them is equall to input number


def find_in_list(entered_list, num, length):
    for i, list_element in enumerate(entered_list):
        temp = num - list_element
        if temp in entered_list:
            temp_index = entered_list.index(temp)
            print(f"{temp} + {list_element} = {num} ")
            print(f"index of {temp}  is {temp_index}")
            print(f"index of {list_element}  is {i}")
            input_list.remove(temp)
            input_list.remove(list_element)

    if length == len(input_list):
        print("sorry! don't have two number for you :))")


input_list = input("please enter numbers for list :").split(",")
input_num = int(input("please enter your number :"))
first_length_list = len(input_list)
input_list = list(map(int, input_list))
find_in_list(input_list, input_num, first_length_list)
