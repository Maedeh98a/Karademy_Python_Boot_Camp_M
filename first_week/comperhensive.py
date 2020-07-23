# in this program we enter the number and calculate square of number
# our goal in this program is that find prime number between input and its squre


def detect_prime(first_number, second_num, list_num, counter):
    for prime in range(first_number, second_num):
        for factor in range(2, (second_num // 2) + 1):
            if prime % factor == 0:
                counter += 1
                if counter > 1:
                    list_num.remove(prime)
                    break
        counter = 0


first_num = int(input("Enter your number:"))
square_num = first_num ** 2
count_factor = 0
all_num = []
for num in range(first_num, square_num):
    all_num.append(num)

detect_prime(first_num, square_num, all_num, count_factor)

print(all_num)
