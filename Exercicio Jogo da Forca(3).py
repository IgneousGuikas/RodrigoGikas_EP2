import turtle

window = turtle.Screen() # limite_x: +-330, Limite_y: +-270
window.setup(width=700,height=540,startx=None,starty=None)
window.bgcolor('lightblue')
window.title('Jogo da Forca')

caneta = turtle.Turtle()
#caneta.hideturtle()
caneta.speed(3)
caneta.penup()
caneta.color('Black')
caneta.pensize(5)

def nome_jogo(turtle):
    turtle.setpos(-95,230)
    turtle.write('Jogo da Forca', font=('Arial',20,'bold'))
    turtle.setpos(0,0)

def desenho_forca(turtle):
    turtle.setpos(-320,-100)
    turtle.pendown()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(25)
    turtle.penup()
    turtle.setpos(-245,-100)
    turtle.pendown()
    turtle.forward(250)
    turtle.right(90)#(-245,150)
    turtle.forward(100)
    turtle.right(90)#(-145,150)
    turtle.forward(25)
    turtle.penup()
    turtle.left(90)#(-145,125)
    turtle.setpos(0,0)

def desenho_cabeca (turtle):
    turtle.setpos(-145,125)
    turtle.left(180)
    turtle.pendown()
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()
    turtle.fillcolor('black')
    turtle.penup()
    turtle.left(180)
    turtle.setpos(0,0)

def desenho_dorso(turtle):
    turtle.setpos(-145,75)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(80)
    turtle.penup()
    turtle.left(90)
    turtle.setpos(0,0)

def desenho_left_arm(turtle):
    turtle.setpos(-145,75)
    turtle.right(135)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.left(135)
    turtle.setpos(0,0)

def desenho_right_arm(turtle):
    turtle.setpos(-145,75)
    turtle.right(45)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.left(45)
    turtle.setpos(0,0)

def desenho_left_leg(turtle):
    turtle.setpos(-145,-5)
    turtle.right(120)
    turtle.pendown()
    turtle.forward(65)
    turtle.penup()
    turtle.left(120)
    turtle.setpos(0,0)

def desenho_right_leg(turtle):
    turtle.setpos(-145,-5)
    turtle.right(60)
    turtle.pendown()
    turtle.forward(65)
    turtle.penup()
    turtle.left(60)
    turtle.setpos(0,0)



    
L = open('entrada.txt','r+',encoding='utf-8')
lista = []

for i in L.readlines():
    s = i.lower().strip()
    if s == '':
        None
    else:
        lista.append(s)
L.close()

nome_jogo(caneta)
desenho_forca(caneta)
desenho_cabeca(caneta)
desenho_dorso(caneta)
desenho_left_arm(caneta)
desenho_right_arm(caneta)
desenho_left_leg(caneta)
desenho_right_leg(caneta)



'''
v = window.textinput('Escolha','Escolha um Letra')
print(v)
'''
window.exitonclick()
