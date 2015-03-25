import turtle
from random import shuffle
import unicodedata
import time


def nome_jogo(turtle):
    turtle.setpos(-95,230)
    turtle.write('Jogo da Forca', font=('Arial',20,'bold'))
    turtle.home()

def desenho_forca(turtle, window_comprimento):
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

def desenho_cabeca (turtle, window_comprimento):
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

def desenho_dorso(turtle, window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,75)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(80)
    turtle.penup()
    turtle.left(90)
    turtle.home()

def desenho_left_arm(turtle, window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,75)
    turtle.right(135)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.left(135)
    turtle.home()

def desenho_right_arm(turtle, window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,75)
    turtle.right(45)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.left(45)
    turtle.home()

def desenho_left_leg(turtle, window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,-5)
    turtle.right(120)
    turtle.pendown()
    turtle.forward(65)
    turtle.penup()
    turtle.left(120)
    turtle.home()

def desenho_right_leg(turtle, window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,-5)
    turtle.right(60)
    turtle.pendown()
    turtle.forward(65)
    turtle.penup()
    turtle.left(60)
    turtle.home()

def desenho_espacos(turtle, letras_palavra, window_comprimento):
    posicoes_letras = []
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
            posicoes_letras.append([turtle.pos(),i])
    turtle.pensize(5)
    turtle.left(180)
    turtle.home()
    posicoes_letras.reverse()
    return posicoes_letras

def desenho_letras(turtle, palavra, posicoes_letras, escolha, window_comprimento, tries,):
    text1 = str(unicodedata.normalize('NFKD',palavra).encode('ASCII','ignore'))
    no_accent = text1[2:len(text1)-1]
    
    coordenada_x = (window_comprimento/-2)+tries*20
    index = []
    
    if escolha in no_accent:
        print(no_accent)
        for x,e in enumerate(no_accent):
            if escolha == e:
                index.append(x)
        for i in index:
            turtle.setpos((posicoes_letras[i][0][0])+15,(posicoes_letras[i][0][1]))
            turtle.write(posicoes_letras[i][1], font=('Arial',20,'bold'))
            turtle.home()
            return 0,index
    else:
        turtle.setpos(coordenada_x+30,-155)
        turtle.write(escolha, font=('Arial',18,'bold'))
        turtle.home()
        return 1,None

def caneta_setup ():
    caneta.hideturtle()
    caneta.speed(100)
    caneta.penup()
    caneta.color('Black')
    caneta.pensize(5)


'''
-------------------------------------------------------------------------------
'''


window = turtle.Screen() # limite_x: +-330, Limite_y: +-270
window.bgcolor('lightblue')
window.title('Jogo da Forca')

caneta = turtle.Turtle()
caneta_setup()



lista_palavras = [] 
L = open('entrada.txt','r+',encoding='utf-8')

for i in L.readlines():
    s = i.lower().strip()
    if s == '':
        None
    else:
        lista_palavras.append(s)
L.close()
'''
-------------------------------------------------------------------------------
'''

letras_palavra = []

if lista_palavras != []:
    shuffle(lista_palavras)
    palavra = lista_palavras[int(len(lista_palavras)/2)]
    
    for i in palavra:
        letras_palavra.append(i)
    letras_palavra.reverse()
    
    comprimento = (len(letras_palavra)*35)*2
    
    del lista_palavras[int(len(lista_palavras)/2)]

    if comprimento <= 500:
        comprimento += 80
        window.setup(width=comprimento,height=540,startx=None,starty=None)
    elif comprimento > 500 and comprimento <= 650:
        comprimento += 30
        window.setup(width=comprimento,height=540,startx=None,starty=None)
    elif comprimento > 650 and comprimento <= 800:
        comprimento -= 30
        window.setup(width=comprimento,height=540,startx=None,starty=None)
    elif comprimento > 800 and comprimento <= 1000:
        comprimento -= 110
        window.setup(width=comprimento,height=540,startx=None,starty=None)
    else:
        comprimento -= 250
        window.setup(width=comprimento,height=540,startx=None,starty=None)
    
    nome_jogo(caneta)
    desenho_forca(caneta, window.window_width())
    
    posicoes_letras = desenho_espacos(caneta, letras_palavra, window.window_width())
    print(posicoes_letras)    
    
    escolha = ''
    tentativas = 0
    acertos = []    
    
    while True:
        escolha = window.textinput('','Escolha uma letra ou chute a palavra')
        
        if escolha == None:
            caneta.setpos(-175,200)
            caneta.write('Jogador desistiu. Volte sempre.', font=('Arial',18,'bold'))
            break
        else:
            if escolha.isalpha() and len(escolha) == 1:
                l = []
                s = 0
                s,l = desenho_letras(caneta, palavra, posicoes_letras, escolha, window.window_width(), tentativas)
                tentativas += s
                acertos.append(l)
            else:
                caneta.setpos(-95,200)
                caneta.write('Escolha Inválida.', font=('Arial',18,'bold'))
                time.sleep(2)
                caneta.reset()
                caneta_setup()
                
                
                nome_jogo(caneta)
                desenho_forca(caneta, window.window_width())
                desenho_espacos(caneta, letras_palavra, window.window_width())
                
        '''
    print(posicoes_letras)
    print()
    print(desenho_letras(caneta, posicoes_letras, 2))
    
    
    '''
    caneta.setpos(-95,0)
    caneta.write('Clique para Sair', font=('Arial',18,'bold'))
    caneta.home()
    window.exitonclick()
'''
-------------------------------------------------------------------------------
'''


palavra = ''

if palavra != '':
    desenho_cabeca(caneta, window.window_width())
    desenho_dorso(caneta, window.window_width())
    desenho_left_arm(caneta, window.window_width())
    desenho_right_arm(caneta, window.window_width())
    desenho_left_leg(caneta, window.window_width())
    desenho_right_leg(caneta, window.window_width())


'''
v = window.textinput('Escolha','Escolha um Letra ')
print(v)
'''
window.exitonclick()
