import turtle
my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
for i in range(0, 30):    # 分成30个步骤
    my_turtle.forward(10)     # 每次步长10
    my_turtle.right(12)       # 360/30 == 12
turtle.mainloop()
