# create a Function with Parameters
# name = "Kelly"
# age = 25
# def demo(name,age):
#     print(name,age)
# demo(name,age)


# Variable length of Arguments (*args)

# def func1(*args):
#     print("Printing value:")
#     for i in args:
#       print(i)
# func1(20,40,60)
# func1(80,100)

# Return Multiple Values from a Function
# a = 40
# b = 10
# def calculation(a,b):
#    x = a + b
#    y = a - b
#    return x, y
# x,y = calculation(a,b)
# print(x,y)

# function with default Argument
# def show_employee(name, salary = 9000):
#     print(name,salary)
# show_employee( "Ben salary:", 12000)
# show_employee( "jessa salary:")

# positional and keyword
def describe_pet(animal_type,pet_name):
    print( " I have a ",animal_type)
    print( "My pet name is",pet_name)
    
describe_pet("hamster", "Harry")
describe_pet(animal_type = "dog", pet_name = "willie")
