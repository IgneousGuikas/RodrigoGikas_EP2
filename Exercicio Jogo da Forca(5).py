import turtle
from random import shuffle

def nome_jogo(turtle,window_comprimento):
    turtle.setpos(-95,230)
    turtle.write('Jogo da Forca', font=('Arial',20,'bold'))
    turtle.home()

def desenho_forca(turtle,window_comprimento):
    coordenada_x1 = (window_comprimento/-2)+30
    turtle.setpos(coordenada_x1,-100)
    turtle.pendown()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(25)
    turtle.penup()
    coordenada_x2 = (window_comprimento/-2)+105
    turtle.setpos(coordenada_x2,-100)
    turtle.pendown()
    turtle.forward(250)
    turtle.right(90)#(-245,150)
    turtle.forward(100)
    turtle.right(90)#(-145,150)
    turtle.forward(25)
    turtle.penup()
    turtle.left(90)#(-145,125)
    turtle.home()

def desenho_cabeca (turtle,window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,125)
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

def desenho_dorso(turtle,window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,75)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(80)
    turtle.penup()
    turtle.left(90)
    turtle.home()

def desenho_left_arm(turtle,window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,75)
    turtle.right(135)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.left(135)
    turtle.home()

def desenho_right_arm(turtle,window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,75)
    turtle.right(45)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.left(45)
    turtle.home()

def desenho_left_leg(turtle,window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,-5)
    turtle.right(120)
    turtle.pendown()
    turtle.forward(65)
    turtle.penup()
    turtle.left(120)
    turtle.home()

def desenho_right_leg(turtle,window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,-5)
    turtle.right(60)
    turtle.pendown()
    turtle.forward(65)
    turtle.penup()
    turtle.left(60)
    turtle.home()

def desenho_espacos(turtle,letras_palavra,window_comprimento):
    coordenada_x = (window_comprimento/2)-30
    turtle.setpos(coordenada_x,-125)
    turtle.left(180)
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
    turtle.left(180)
    turtle.home()







caneta = turtle.Turtle()
caneta.hideturtle()
caneta.speed(5)
caneta.penup()
caneta.color('Black')
caneta.pensize(5)

palavra = ''


lista = [] 
L = open('entrada.txt','r+',encoding='utf-8')

for i in L.readlines():
    s = i.lower().strip()
    if s == '':
        None
    else:
        lista.append(s)
L.close()


window = turtle.Screen() # limite_x: +-330, Limite_y: +-270

window.bgcolor('lightblue')
window.title('Jogo da Forca')


a = 0
letras_palavra = []

if a < 11:
    shuffle(lista)
    palavra = lista[int(len(lista)/2)]
    del lista[int(len(lista)/2)]
    
    for i in palavra:
        letras_palavra.append(i)
    letras_palavra.reverse()
    print(letras_palavra)
    
    comprimento = ((len(letras_palavra)*35)+25)*2
    print(comprimento)
    
    window.setup(width=comprimento,height=540,startx=None,starty=None)
    desenho_espacos(caneta,letras_palavra,window.window_width())
    






if palavra != '':
    nome_jogo(caneta,window.window_width())
    desenho_forca(caneta,window.window_width())
    desenho_cabeca(caneta,window.window_width())
    desenho_dorso(caneta,window.window_width())
    desenho_left_arm(caneta,window.window_width())
    desenho_right_arm(caneta,window.window_width())
    desenho_left_leg(caneta,window.window_width())
    desenho_right_leg(caneta,window.window_width())


'''
v = window.textinput('Escolha','Escolha um Letra')
print(v)
'''
window.exitonclick()
