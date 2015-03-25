import turtle
from random import shuffle

palavra = ''
lista = []

def nome_jogo(turtle,window):
    turtle.setpos(-95,230)
    turtle.write('Jogo da Forca', font=('Arial',20,'bold'))
    turtle.home()

def desenho_forca(turtle,window):
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
    turtle.home()

def desenho_cabeca (turtle,window):
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
    turtle.home()

def desenho_dorso(turtle,window):
    turtle.setpos(-145,75)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(80)
    turtle.penup()
    turtle.left(90)
    turtle.home()

def desenho_left_arm(turtle,window):
    turtle.setpos(-145,75)
    turtle.right(135)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.left(135)
    turtle.home()

def desenho_right_arm(turtle,window):
    turtle.setpos(-145,75)
    turtle.right(45)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.left(45)
    turtle.home()

def desenho_left_leg(turtle,window):
    turtle.setpos(-145,-5)
    turtle.right(120)
    turtle.pendown()
    turtle.forward(65)
    turtle.penup()
    turtle.left(120)
    turtle.home()

def desenho_right_leg(turtle,window):
    turtle.setpos(-145,-5)
    turtle.right(60)
    turtle.pendown()
    turtle.forward(65)
    turtle.penup()
    turtle.left(60)
    turtle.home()

def desenho_espacos(turtle,letras_palavra):
    turtle.setpos(-30,-125)
    turtle.pensize(3)
    for i in letras_palavra:
        if i == ' ':
            turtle.forward(35)
        else:
            turtle.pendown()
            turtle.forward(30)
            turtle.penup()
            turtle.forward(5)
    turtle.pensize(5)
    turtle.home()







window = turtle.Screen() # limite_x: +-330, Limite_y: +-270
window.setup(width=700,height=540,startx=None,starty=None)
window.bgcolor('lightblue')
window.title('Jogo da Forca')

caneta = turtle.Turtle()
caneta.hideturtle()
caneta.speed(3)
caneta.penup()
caneta.color('Black')
caneta.pensize(5)



    
L = open('entrada.txt','r+',encoding='utf-8')

for i in L.readlines():
    s = i.lower().strip()
    if s == '':
        None
    else:
        lista.append(s)
L.close()





a = 0
letras_palavra = []

if a < 11:
    shuffle(lista)
    palavra = lista[int(len(lista)/2)]
    del lista[int(len(lista)/2)]
    for i in palavra:
        letras_palavra.append(i)
    print(letras_palavra)
    desenho_espacos(caneta,letras_palavra)





print(window.window_width())




if palavra != '':
    nome_jogo(caneta,window)
    desenho_forca(caneta,window)
    desenho_cabeca(caneta,window)
    desenho_dorso(caneta,window)
    desenho_left_arm(caneta,window)
    desenho_right_arm(caneta,window)
    desenho_left_leg(caneta,window)
    desenho_right_leg(caneta,window)



'''
v = window.textinput('Escolha','Escolha um Letra')
print(v)
'''
window.exitonclick()
