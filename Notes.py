"""#print("Hello, world!")

#Forever


# Two plus two is four, minus one that's three, quick maths

print("2 + 2 is 4")
tpf = 2 + 2
print(tpf)
print("minus 1 that's 3")
qm = tpf - 1
print(qm)
print("quick maths")

print(13%5)
# "%" is a modulus

car_name = "The Wiebe Moile"
car_type = "BMW"
car_cylinders = 8
car_mpg = 5000.9

print("I have a car called %s. It's a %s." % (car_name, car_type))
#Watch the order

print("memes")
response = input(">_")
print("yah i like %s too!111" % response)

age = input("How old are you little boye?")
print("%s! That's really old. You belong in a retirement home." % age)"""

"""
def print_hw():
    print("Hello world")
    print("Enjoy the day.")


print_hw()


def say_hi(name):
    print("Hello %s" % name)
    print("Coding is lit af")


say_hi("beepboop")"""


"""def print_info(name, age):
    print("%s is %d years old" % (name, age))
    age += 1
    print("Next year, %s will be %d years old" % (name, age))


print_info("Bob", 2)


def algebra_hw(x):
    return x**3 + 4*x**2 + 7 * x - 4


print(algebra_hw(3))
print(algebra_hw(4))
print(algebra_hw(5))
print(algebra_hw(6))
print(algebra_hw(7))
"""

def grade_calculator(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

print (grade_calculator(40))