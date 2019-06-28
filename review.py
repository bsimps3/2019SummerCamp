import random
import turtle

var1 = 10
var2 = 20
print(var1 + var2)

var3 = var1
print(var3)

print("Hey", var1)

print(var1*var2)
print(var1**var2)
print(var1-var2)
print(var1/var2)
print(var1%var2)

#output of True/False
print(var1 == var2)
print(var1 > var2)
print(var1 < var2)
print(var1 != var2)
print(var1 >= var2)
print(var1 <= var2)

#loops
x = 0
while x < 10:
    print(x)
    x = x + 1

while True:
    print("get rekt")
    if(x < 100):
        break               #stops the while loop

list = ["a", "b", "c"]
for letter in list:
    print(letter)

for number in range(3):
    print( list[number] )

# logic

if x < 100:
    print("haha")
elif x == 58:
    print("x is 42, jk, it isn't")
elif x == 20:
    print("x is not 20, jk, it is")
else:
    print("None of those were true")

#random stuff

x = random.randint(0,10)  #gives a random number  0<= x <= 10

#functions

def name_of_function(input_stuff):
    return input_stuff + "now there's more"

#somewhere else in your code
name_of_function("hey")

#turtle commands,  google:  3.7 turtle python
turtle.speed(10)
turtle.shape("turtle")
turtle.forward(100)
turtle.left(90)
turtle.right(90)
turtle.backward(100)

def go_forward():
    turtle.forward(100)

turtle.listen()
turtle.onkey(go_forward, "Up")

turtle.done()

turtle.penup()
turtle.pendown()
turtle.width(5)
