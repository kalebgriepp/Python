# testing commit

# def find_max(num_1, num_2):
#    max_val = 0.0
#
#    if (num_1 > num_2):  # if num1 is greater than num2,
#       max_val = num_1   # then num1 is the maxVal.
#    else:                # Otherwise,
#       max_val = num_2   # num2 is the maxVal
#    return max_val
#
# max_sum = 0.0
#
# num_a = float(input())
# num_b = float(input())
# num_y = float(input())
# num_z = float(input())
# max_sum = find_max(num_a, num_b) + find_max(num_y, num_z)
# #apparently overthinking means nothing in programming....ugh
# def find_max(num_a, num_b, num_y, num_z):
#     if num_a > num_b:
#         if num_y > num_z:
#             max_sum = num_a + num_y
#         elif num_y < num_z:
#             max_sum = num_a + num_z
#     if num_a < num_b:
#         if num_y > num_z:
#             max_sum = num_b + num_y
#         elif num_y < num_z:
#             max_sum = num_b + num_z
#     return find_max(max_sum)
#
# print('max_sum is:', max_sum)

#########################
# num_one = int(input())
# num_two = int(input())
# print(num_one)
# while num_one <= num_two:
#     print(num_one + 10, end=' ')
#     num_one = num_one + 10
#     if num_two <= num_one:
#         print("Second integer can't be less than the first.")
#     else:
#         break
#
#
# from sys import exit
#
# while True:
#     x = int(input('Enter a number between 0 and 9: '))
#     if x == 3:
#         exit()
#
password = input()

# for char in password:
#     char = password.replace("i", "!")
#     char = password.replace("a","@")
#     char = password.replace("m", "M")
#     char = password.replace("B", "8")
#     char = password.replace("o", ".")
#     char = password + ("q*s")
# print(char)


# def mph_and_minutes_to_miles(hours_traveled, miles_traveled):
#     hours_traveled = minutes_traveled / 60.0
#     miles_traveled = hours_traveled * miles_per_hour
#     return mph_and_minutes_to_miles
#
#
# miles_per_hour = float(input())
# minutes_traveled = float(input())
#
# print('Miles: {:f}'.format(mph_and_minutes_to_miles(miles_per_hour, minutes_traveled)))

# def build_list():
#     number = int(input())
#     store_numbers = []
#     for n in range(number):
#         store_numbers.append(int(input()))
#     return store_numbers
#
#
# def is_list_even(my_list):
#     for number in my_list:
#         if number // 2 == 1:
#             return False
#         else:
#             return True
#
#
# def is_list_odd(my_list):
#     for number in my_list:
#         if number // 2 == 0:
#             return False
#         else:
#             return True
#
# if __name__ == '__main__':
#     store_numbers = build_list()
#     if is_list_even:
#         print('all even')
#         print(is_list_even(store_numbers))
#     if is_list_odd:
#         print('all odd')
#         print(is_list_odd(store_numbers))
#     else:
#         print('not even or odd')

## For 7.6 Lab
user_input = input()
tokens = user_input.split()

if len(tokens) == 2:
    print('%s, %s' % (tokens[1], tokens[0]))

if len(tokens) == 3:
    print('%s, %s %s.' % (tokens[2], tokens[0], tokens[1][0]))