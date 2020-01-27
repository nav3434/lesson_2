#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# number = 1
# while number <= 5:
#     print(number, 0)
#     number = number + 1

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# b = 0
# i = 1
# while i <= 10:
#     a = input ('Input digit ')
#     i = i + 1
#     if int(a) == 5:
#         b = b + 1
# print ('you input ', b, 'digit 5')
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# result = 1
#
# for i in range(1, 11):
#     result*=i
# print(result)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# number = 12345
# result = 0
#
# while number > 0:
#     result = result + number%10
#     number = number//10
# print (result)



'''
Задача 7
Найти произведение цифр числа.
'''
# number = 123
# result = 1
#
# while number > 0:
#     result = result * number%10
#     number = number//10
# print(result)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# number = 129456
# a = number%10
# while number >0:
#     number = number//10
#     a = number%10 if a < number%10 else a
# print(a)



'''
Задача 10
Найти количество цифр 5 в числе
'''
# number = 12525525
# b = 0
#
# while number >0:
#     b = b + 1 if number%10 == 5 else b
#     number = number//10
# print(b)
