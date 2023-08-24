import turtle
t = turtle.Turtle()
t.screen.bgcolor('black')
t.pensize(2)
t.color('green')
t.left(90)
t.backward(100)
t.speed(1000)
t.shape('turtle')

def tree(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.color('orange')
        t.circle(3)
        t.color('brown')
        t.left(40)
        tree(3*i/4)
        t.right(80)
        tree(3*i/4)
        t.left(40)
        t.backward(i)
tree(100)
turtle.done()        
