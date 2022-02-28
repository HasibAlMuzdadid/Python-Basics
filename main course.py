# print("1 is a number")
# print(300.99)
# print(24 * 23 * 45)
# print("30 days are " + str(30 * 24 * 60) + " seconds")
# print(f"30 days are {30 * 24 * 60} minutes")

# calculation_to_unit = 24 * 60
# name_of_unit = "minutes"

# print(f"30 days are {30 * calculation_to_unit} {name_of_unit}")
# print(f"40 days are {40 * calculation_to_unit} {name_of_unit}")
# print(f"50 days are {50 * calculation_to_unit} {name_of_unit}")
# print(f"60 days are {60 * calculation_to_unit} {name_of_unit}")


# ..................using function


# def day_to_unit(days):
#     print(f"{days} days are {days * calculation_to_unit} {name_of_unit}")
#     print("well done")


# day_to_unit(30)
# day_to_unit(40)
# day_to_unit(50)
# day_to_unit(60)


# def day_to_unit(days, message):
#     print(f"{days} days are {days * calculation_to_unit} {name_of_unit}")
#     print(message)


# day_to_unit(30, "hi")
# day_to_unit(40, "hello")
# day_to_unit(50, "awesome")
# day_to_unit(60, "well done")


# def day_to_minute(days):
#     return f"{days} days are {days * calculation_to_unit} {name_of_unit}"


# my_var = day_to_minute(30)
# print(my_var)


# ......................input....taken


# def day_to_minute2(days):
#     return f"{days} days are {days * calculation_to_unit} {name_of_unit}"


# user_input = input("please enter the number of days :\n")
# user_input_converted_in_number = int(user_input)
# calculated_value = day_to_minute2(user_input_converted_in_number)
# print(calculated_value)


# .............................if......else


# def day_to_minute3(days):
#     if days > 0:
#         return f"{days} days are {days * calculation_to_unit} {name_of_unit}"
#     elif days == 0:
#         return "you've entered 0, please enter a valid positive number!"
#     else:
#         return "you entered a negative number, please enter a valid positive number!"
#
#
# user_input3 = input("please enter the number of days :\n")
# user_input_converted_in_number3 = int(user_input3)
# calculated_value3 = day_to_minute3(user_input_converted_in_number3)
# print(calculated_value3)


# .........................input validation


# def day_to_minute4(days):
#     if days > 0:
#         return f"{days} days are {days*calculation_to_unit} {name_of_unit}"
#     elif days == 0:
#         return "you have entered a zero, please enter a valid positive number"


# user_input4 = input("please enter the number of days:\n")
# if user_input4.isdigit():
#     user_input_converted_in_number4 = int(user_input4)
#     calculated_value4 = day_to_minute4(user_input_converted_in_number4)
#     print(calculated_value4)
# else:
#     print("you haven't entered a positive valid number, please enter one!")


# ...................input validation by using function


# def day_to_minute5(days):
#     if days > 0:
#         return f"{days} days are {days * calculation_to_unit} {name_of_unit}"
#     elif days == 0:
#         return "you have entered a zero, please enter a valid positive number"
#

# def validate_and_execute():
#     if user_input5.isdigit():
#         user_input_converted_in_number5 = int(user_input5)
#         calculated_value5 = day_to_minute5(user_input_converted_in_number5)
#         print(calculated_value5)
#     else:
#         print("you haven't entered a valid positive number, please enter one!")
#
#
# user_input5 = input("please enter the number of days:\n")
# validate_and_execute()


# .................nested if in input validation


# def day_to_minute6(days):
#     return f"{days} days are {days * calculation_to_unit} {name_of_unit}"


# def validate_and_execute2():
#     if user_input6.isdigit():
#         user_input_converted_in_numbers6 = int(user_input6)
#         if user_input_converted_in_numbers6 > 0:
#             calculated_value6 = day_to_minute6(user_input_converted_in_numbers6)
#             print(calculated_value6)
#         elif user_input_converted_in_numbers6 == 0:
#             print("you have entered a zero, please enter a valid positive number!")
#     else:
#         print("you have entered an invalid number, please enter a valid positive number.")


# user_input6 = input("please enter the number of days:\n")
# validate_and_execute2()


# ............try.........except


# def day_to_minute7(days):
#     return f"{days} days are {days * calculation_to_unit} {name_of_unit}"
#
#
# def validate_and_execute3():
#     try:
#
#         user_input_converted_in_numbers7 = int(user_input7)
#         if user_input_converted_in_numbers7 > 0:
#             calculated_value7 = day_to_minute7(user_input_converted_in_numbers7)
#             print(calculated_value7)
#         elif user_input_converted_in_numbers7 == 0:
#             print("you have entered zero, please enter a valid positive number!")
#         else:
#             print("you have entered a negative number, please enter a valid positive number!")
#
#     except ValueError:
#         print("you have entered an invalid number!!!!")
#
#
# user_input7 = input("please enter the number of days:\n")
# validate_and_execute3()


# ................while.........do.....


# def day_to_minute8(days):
#     return f"{days} days are {days * calculation_to_unit} {name_of_unit}"
#
#
# def validate_and_execute4():
#     try:
#
#         user_input_converted_in_numbers8 = int(user_input8)
#         if user_input_converted_in_numbers8 > 0:
#             calculated_value8 = day_to_minute8(user_input_converted_in_numbers8)
#             print(calculated_value8)
#         elif user_input_converted_in_numbers8 == 0:
#             print("you have entered zero, please enter a valid positive number!")
#         else:
#             print("you have entered a negative number, please enter a valid positive number! ")
#
#     except ValueError:
#         print("you have entered an invalid number!!!!")
#
#
# user_input8 = ""
# while user_input8 != "exit":
#     user_input8 = input("please enter the number of days:\n")
#     validate_and_execute4()


# ........list.....sequential....


# months = ['january', 'february', 'march']
# print(months[2])
# months.append('april')
# print(months)
# print(months[3])
# months.remove('january')
# print(months)


# .............for...lst.......


# def day_to_minute9(days):
#     return f"{days} days are {days*calculation_to_unit} {name_of_unit}"
#
#
# def validate_and_execute5():
#     try:
#
#         user_input_converted_in_numbers9 = int(number_of_days)
#         if user_input_converted_in_numbers9 > 0:
#             calculated_value9 = day_to_minute9(user_input_converted_in_numbers9)
#             print(calculated_value9)
#         elif user_input_converted_in_numbers9 == 0:
#             print("you have entered a zero, please enter a valid positive number!")
#         else:
#             print("you have entered a negative number, please enter a valid positive number!")
#
#     except ValueError:
#         print("you have entered an invalid number!!!!")
#
#
# user_input9 = ""
# while user_input9 != "exit":
#     user_input9 = input("please enter the number of days separated by comma:\n")
#     for number_of_days in user_input9.split(","):
#         validate_and_execute5()


# .............set...not..sequential..........


# months = {'january', 'february', 'march'}
# print(months)
# months.add('april')
# print(months)
# months.remove('february')
# print(months)


# ..................set........for......not..sequential.........


# def day_to_minute10(days):
#     return f"{days} days are {days*calculation_to_unit} {name_of_unit}"
#
#
# def validate_and_execute6():
#     try:
#
#         user_input_converted_in_numbers10 = int(number_of_days)
#         if user_input_converted_in_numbers10 > 0:
#             calculated_value10 = day_to_minute10(user_input_converted_in_numbers10)
#             print(calculated_value10)
#         elif user_input_converted_in_numbers10 == 0:
#             print("you have entered a zero, please enter a valid positive number!")
#         else:
#             print("you have entered a negative number, please enter a valid positive number!")
#
#     except ValueError:
#         print("you have entered an invalid number!!!!")
#
#
# user_input10 = ""
# while user_input10 != "exit":
#     user_input10 = input("please enter the number of days separated by comma:\n")
#
#     print(user_input10.split(","))
#     print(set(user_input10.split(",")))
#
#     for number_of_days in set(user_input10.split(",")):
#         validate_and_execute6()


# ............list....dictionary.......


# my_list = ['20', '45', '32']
# print(my_list[1])
#
# my_dictionary = {"days": 20, "unit": "hours", "message": "hello everyone"}
# print(my_dictionary["days"])
# print(my_dictionary["unit"])
# print(my_dictionary["message"])


# .................dictionary............


def day_to_unit11(days, conversion_unit):
    if conversion_unit == "hour":
        return f"{days} days are {days*24} hours"
    elif conversion_unit == "minute":
        return f"{days} days are {days*24*60} minutes"
    else:
        return "you have entered unsupported conversion unit"


def execute_and_validate7():
    try:

        user_input_converted_in_numbers11 = int(days_and_unit_dictionary["days"])
        if user_input_converted_in_numbers11 > 0:
            calculated_value11 = day_to_unit11(user_input_converted_in_numbers11, days_and_unit_dictionary["unit"])
            print(calculated_value11)
        elif user_input_converted_in_numbers11 == 0:
            print("you have entered a zero, please enter a valid positive number!")
        else:
            print("you have entered a negative number, please enter a valid positive number!")

    except ValueError:
        print("you have entered an invalid number!!!!")


user_input11 = ""
while user_input11 != "exit":
    user_input11 = input("please enter the number of days and unit separated by colon:\n")
    days_and_unit = user_input11.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    execute_and_validate7()