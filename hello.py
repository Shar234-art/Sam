# # # n ='8'
# # # print(int(n)+2)
# # # x = 4 
# # # x += 3
# # # x *= 2
# # # print(x)
# # # text = 'python'
# # # print('py' in text,'z' not in text)
# # # a = [1,2]
# # # b = a
# # # c = [1,2]
# # # print(a is b, a is c, a == c)
# # # x = 10
# # # print(x > 5 and x < 15, not x ==10)
# # # name = 'Asha'
# # # score = 92
# # # print(f'{name}:{score}')
# # # x = 2
# # # y = 3
# # # print(x ** y + 4//3)
# # student_name = 'Ravi'
# # print(student_name)
# # is_active = True 
# # print(is_active)
# # age = input('Enter age:')
# # print(age)
# # print('Python','Basics',sep='-')
# # score = 70
# # score >= 40
# # print('Pass')
# day = 'Wenesday'
# if day == 'Sunday':
#     print("Holiday")
# elif day == 'Saturday':
#     print("Holiday")
# elif day == 'Monday':
#     print(":)")
# elif day == 'Wenesday':
#     print("It is wenesday")
# age = 16
# if age >= 18:
#     print("ADULT")
# else:
#     print("NOT ADULT")
# Name = 'surbhi sharma'
# if Name >= 'Sharma':
#     print("Name")
# else:
#     print("surname")
# num = int(input("Enter a number:"))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")

# num1 = int(input("Enter your number:" ))
# num2 = int(input("Enter your number:"))
# sum = num1 + num2
# if sum >=10 and sum<=20:
#     print(15)
# else:
#     print(0)
# num = int(input("Enter your number:"))
# print(((5*num)/9)-32)
# num1 = int(input("ENTER YOUR NUMBER:"))
# print(((9*num1)/5)+32)
# num1 = int(input("Enter your value:"))
# num2 = int(input("Enter your value:"))
# if num1>num2:
#     print("first number is greater")
# elif num1<num2:
#     print("second number is greater")
# a = int(input("Enter your value:"))
# if a % 2==0 and a % 5==0:
#     print("Divisible by both 2 and 5")
# elif a % 2==0:
#     print("Divisible by 2")
# elif a % 5==0:
#     print("Divisible by 5")
# else:
#     print("Not divisible by either")
# a = 90
# b = 30
# c = 60
# if a>=b:
#     if a>=c:
#         print("a is greater")
#     else:
#         print("b is greater")
# elif b>=a:
#     if b>=c:
#         print("b is greater")
#     else:
#         print("c is greater")
# num = int(input("ENTER YOUR NUMBER:"))
# if num%2 ==0:
#     print("this number is even")
# else:
#     print("this number is odd")
# # for i in (range(0,100,2)):
#     print(i)
# for i in (range(1,101,2)):
#     if i % 2 !=0:
#         print(i, end=" ")
# for i in (range(0,100,2)):
#     if i % 2 ==0:
#         print(i, end=" ")
# for i in (range(1,11)):
#     print('100', "x" ,i, "=",100*i, "  ,  "   '300', "x" ,i, "=",300*i)
# print("A","B",sep=":",end=".")
# result = int("9")+ 1
# print(type(result))
# a = 3
# b = 4
# print(a + b * 2)
# temperature = 15
# if temperature > 25:
#     print("Hot")
# elif temperature >= 15:
#     print("cool")
# else:
#     print("cold")
# colors = ["red", "blue"]
# for color in colors:
#     print(color)
# for number in range(2,10,2):
#     print(number)

# name = input('enter your name:')
# city = input('enter your city:')
# print(f"{name} lives in {city}.")
# n = int(input("Enter a positive integer n:"))
# total = 0
# for i in range(1, n + 1):
#     total += i
#     print("Total:", total)
# user = "surbhi"
# password = 3456
# if user == "surbhi":
#     if password == 345:
#         print("authorized")
#     else:
#         print("password is not matched")
# else:
#     print("not authorized")
# for i in range(6,1,-1):
#     print()
#     for j in range(1,i):
#         print(j, end="")

# total = 1
# for i in range(1,100):
#     total *= i
# print(total)
# i = 1
# while i <= 6:
#     print(i)
#     i -= 1
# i = 1
# for i in range(1,6):
#     print()
#     for j in range(i):
#         print(i, end='')
#         i += 1
# # i = 0
# while i < 100:
#     if i % 2 != 0:
#         print(i)
#     i += 1
# i = 1
# while i < 5:
#     print("sona")
#     i += 1
# user_password = ""
# count = 0
# while user_password != 'python123' and count < 3:
#     user_password = input("Enter password:")
#     count += 1
#     if user_password == 'python123':
#        print("Access Granted")
#     else:
#        print("Wrong password")
# if user_password != 'python123':
#     print("Account locked")
# positive = 0
# negative = 0
# zero = 0
# num = 1
# count = 0
# while num != num and count < 10:
#     num = int(input("Enter your number:"))
#     num += 1
#     count += 1
#     if num < 0:
#         print("positive")
#     if num < 0:
#         print("negative")
#     if num == 0:
#         print("zero")



# user = ""
# count = 0
# while user.lower() != 'yes' and count < 5:
#     user = input("Enter your input:")
#     count += 1
#     if user.lower() == "yes":
#         print("correct")
#     else:
#         print("try again")
# if user.lower() != "yes":
#     print("attempted over")
# num = 0
# while num < 20:
#     num += 1
#     if num > 10:
#         break
#     print(num)
#     if num % 4 == 0:
#         continue
#     print(num)

        
        
# num = 0
# while num < 30:
#     num += 1
#     if num % 3 == 0:
#         continue
#     print(num) 
# array = [1,2,3,4,5,6,7,8,9,' hi','surbhi']
# (array.append('mona'))
# print(array)

# array = [1,2,3,4,5,6,6,7,8,9,'hello','world','sona']
# (array.remove('sona'))
# print(array)

# a = [2,3,4,5,6,6,7,7,8,8,'hi','subhi']
# (a.pop(8))
# print(a)

# a = [1,2,3,4,5,6,7,8,9]
# a[0] = 20
# a[4] = 15
# print(a)
# print(len(a))

# fruits = ['apple','banana','mango']
# fruits[1] = 'kivi'
# print(fruits)

# fruits = ['apple','banana','mango']
# (fruits.append('orange'))
# print(fruits)

# fruits = ['apple','banana','mango']
# fruits[0] = 'grape'
# print(fruits)

# fruits = ['apple','banana','mango']
# fruits.insert(0,'grape')
# print(fruits)

# fruits = ['apple','banana','mango']
# (fruits.remove('mango'))
# print(fruits)
# print('Flow','Control',sep='*',end='!')
# x = 7
# y = 2
# # print(x//y,x%y,x**y)
# marks = 68
# if marks >= 75:
#    print('distinction')
# elif marks >= 60:
#    print('First class')
# elif marks >= 40:
#    print('pass')
# else:
#    print('Fail')
# x = 15
# if x > 10:
#    if x % 2 == 0:
#       print('big even')
#    else:
#       print('big odd')
# else:
#    print('small')
# for i in range(1,10,3):
#    print(i,end=' ')
# for i in range(5,0,-1):
#    if i % 2 == 0:
#       continue
#    print(i,end=' ')
# count = 0
# while count < 3:
#    count += 1
#    print(count * 2)
# for ch in 'python':
#    if ch == 'h':
#       break
#    print(ch,end= '')
# for i in range(1,4):
#    for j in range(1,i + 1):
#       print(j,end='')
#    print()
# total = 0
# for n in range(1,8):
#    if n % 3 == 0:
#       continue
#    total += n
# print(total)
# n = 305
# digits = 0
# while n > 0:
#    n //= 10
#    digits += 1
# print(digits)
# out = ''
# for ch in 'programming':
#    if ch == 'i':
#       break
#    if ch == 'a':
#       continue
#    out += ch
# print(out)
# x = 1
# while x < 50:
#    x *= 2
# print(x)

# age = int(input('Enter age:'))
# if age >= 18:
#    print('adult')
# total = 50
# print(total,'total:')
# x = 10
# if x == 10:
#    print('ten')
# secret_number = 40
# attemptes = 0
# while attemptes < 7:
#    guess = int(input("Enter your guess 0 - 50:"))
#    attemptes += 1
#    if guess > secret_number:
#       print(" Too high")
#    elif guess < secret_number:
#       print("Too low ")
#    elif guess == secret_number:
#       print("correct")
#       break
# array = [1,2,3,4,5,6,7,8,9,0]  
# for i in array:
#    if i % 2 == 0:
#       print(i)
# a = "hello"
# print(len(a))
# print(a[::-1])
# print(a[0:4])
# a = 'hello'
# b = 'world'
# print(a + b)
# a = "hello"
# for i in a:
#    print(i, end=" ")
# ages = [19,22,19,24,20,25,26,24,25,24]
# ages.sort()
# print("sorted list:",ages)
# # find the minimum and maxmimum ages
# print("maxmimum age:",max(ages))
# print("minimum ages:",min(ages))
# # add the min age and max age
# ages.append(max(ages))
# ages.append(min(ages))
# print("updated list:",ages)
# # average age
# ages = sum(ages)/len(ages)
# print("average age:", ages)
# # range of the ages
# age_range = max(ages)-min(ages)
# print(age_range)
# find the error
# fruits = ['apple', 'mango','kivi']
# for i in range(len(fruits)):
#     print(fruits[i].upper())

# reverse a string
# a = ("Surbhi")
# print(a[::-1])


# a = " hello Surbhi"
# i = len(a)-1
# reverse = ""
# while i >= 0:
#     reverse += a[i]
#     i -= 1
# print(reverse)

# a = "hello surbhi"
# i = len(a) - 1
# reverse = ""
# for i in a:
#     reverse = i + reverse
# print(reverse)

# person = {'frist_name':"Surbhi",
#           'last_name':"Sharma",
#           'age':22,
#           'skills':["singing","dancing","drawing"],
#           'address':{'state':'UP',
#                      'city':{'name':'pilibhit'}}}
# print(person['address']['state']) 
# person['age'] = 35
# print(person['age'])
# person['skills'][1]= 'night out'
# print(person['skills'])
# print(person[0])
# print(len(person))
# for key, value in person.items():
#     print((key, ":", value))
# del person
# print(person)
# print(person.keys())
# print(person.values())
# person.pop('last_name')
# print(person)
# person.popitem()
# print(person)
# del person
# print(person)
# for key in person.keys():
#     print(key)
# for value in person.values():
#     print(value)



# Dog = {}
# print(Dog)
# Dog = {'Name' : "Luna",
#        'color': "white",
#        'breed': "pomerian",
#        'legs': 4,
#        'age': 2}
# print(Dog)



# student = {'first_name': "Surbhi",
#            'last_name' : "Sharma",
#            'gender' : "female",
#            'age' : 22,
#            'marital status': "Unmarried",
#            'skills' : ["singing","dancing","drawing"],
#            'country' : "India",
#            'address': "pilibhit",
#            'city' : "pilibhit"} 
# print(len(student))
# print(student['skills'])
# print(type(student['skills']))
# student['skills'].append("night out")
# print(student['skills'])
# print(student.keys())
# print(student.values())
# print(student.items())
# # for key,value in student.items():
# #     print((key,":",value))
# student.pop('address')
# print(student) 
# del student
# print(student)  
#  
# def Surbhi(name):
#     print(name,"says hello")
# name = input("Enter your name:")
# name2 = input("Enter your name:")
# name3 = input("Enter your name:")
# Surbhi(name)
# Surbhi(name2)
# Surbhi(name3)

# def Surbhi(name):
#     print(f"{name} says hello everyone.")
# Surbhi("Vikas")
# Surbhi("Somya")
# Surbhi("Surbhi")

# def calculator(option):
#     num1 = int(input("Enter first number:"))
#     num2 = int(input("Enter second number:"))
#     option = input("Enter +,- , * ,or / :")
#     return num1+num2,num1-num2, num1*num2,num2/num1
# print(calculator("option"))

# def hello():
#     num = 10
#     print(num)
# hello()

# num = 20
# def hello():
#     num = 10
#     print(num)
# def greet():
#     num = 35
#     print(num)
# hello()
# greet()

# a = 30
# b = 25
# def add():
#     return a + b
# print("ADD:",add())
# def subt():
#     return a - b
# print("SUBT:",subt())
# def mult():
#     return a * b
# print("MULT:",mult())
# def divi():
#     return a / b
# print("Divi:",divi())

# def is_even(a):
#     if a % 2 == 0:
#         return ("number is even.")
#     else:
#         return ("number is odd.")
# print(is_even(8))

# num = [1 ,2, "hello" ,3 ,4 ,5, 0.5 ]
# def moon(num):
#     if num == 0:
#         return(" same data type.")
#     else:
#         return("not matched.")
# print(type(num))

# lst = [1,2,3 , "hello",10,20]
# def check(lst):
#     for item in lst:
#         if type(item) == type(lst[0]):
#             return ("True")
#         return ("false")
# print(check([lst]))

# def greet():
#     return 'hello'

# x = 12
# y = 4
# try:
#     z = x / y
#     print(z)
# except:
#     print("can divided by 4")

# a = 3
# b = 0
# try:
#     c = a / b
#     print(c)
# except:
#     print("can't be devided")

# def fan(num):
#     if num < 5:
#         result = num/(num-5)
#     print(result)
# try:
#     fan(0)
#     fan(1)
#     fan(2)
#     fan(3)
#     fan(4)
# except NameError as n:
#     print(n)


# my_dict = {"a": 2, 'b': 4, 'c': 'hello','d': 3}
# try:
#     print(mydict)
# except NameError:
#     print("check spelling")
# except TypeError:
#     print("check typing mistake")
# except AttributeError:
#     print("check some python numeric value")

# first question.
# lenth = 10
# width = 5
# try:
#     area = lenth * width
#     print(area)
# except ValueError:
#     print('enter valid number')


# # # second question.
# a = 10
# b = 0
# try:
#     result = a/b
#     print(result)
# except ZeroDivisionError:
#     print("can't be divided")
# except ValueError:
#     print("enter valid number")
# finally:
#     print("finally it's done")


# third question.
# a = "hello" 
# b = "no"
# a = [10,20,40]
# try:
#     print(a[4])    
# except IndexError:
#     print("check index")
# except ValueError:
#     print("check value")
# finally:
#     print("finally it's done")



 




    
   





    
      
   
    




    
        

    









































   
    


    










    

















    




























  
