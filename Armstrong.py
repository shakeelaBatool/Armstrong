number = int(input(" Enter the number. "))
str_number = str(number)
num_digit = len(str_number)
sum_power = 0
tmp_num = number
while tmp_num > 0 :
      digit = tmp_num % 10
      sum_power += digit ** num_digit
      tmp_num //= 10
if sum_power == number:
    print(f"{number} is a Armstrong number")    
else:
    print(f"{number} is a not Armstrong number")

