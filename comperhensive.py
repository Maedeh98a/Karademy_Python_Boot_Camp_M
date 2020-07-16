# input number , then detect prime number bitween that number and squre of number, show prime number in list 

first_num = int(input("enter your number:"))
squre_num = first_num ** 2
count_factor = 0
all_num = []
for num in range(first_num, squre_num):
    all_num.append(num)

for prime in range(first_num, squre_num):
    for factor in range(2,(squre_num//2)+1):
        if prime % factor == 0:
            count_factor += 1
            if count_factor > 1:
                all_num.remove(prime)
                break
    count_factor = 0
print(all_num)

                
                

