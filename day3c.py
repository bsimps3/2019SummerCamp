import turtle

turtle.shape('turtle')
turtle.speed(18)
turtle.width(5)  #number 1-10

color_list = ['Pink', 'Red', 'Blue', 'Purple', 'Orange', 'Violet', 'Green']


num = 0
while num < 7:
    turtle.pencolor(color_list[num])
    turtle.forward(10)
    num = num + 1



turtle.done()





