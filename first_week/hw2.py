#in this program we enter the list of numbers 
#then we enter number
#we find tow number in list that summation of them is equall to input number

input_list = input("please input numbers for list :").split(",")
input_num = int(input("please enter your number :"))

for list_index in range(len(input_list)):
    temp = input_num - (int(input_list[list_index]))
    if str(temp) in input_list:
        print("numbers and index are :\n")
        print("first number and it's index: ",input_list[list_index],list_index)
        print("second number and it's index: ",temp, input_list.index(str(temp)))
        break
else:
    print("sorry! don't have two number for you :))")
    
    
