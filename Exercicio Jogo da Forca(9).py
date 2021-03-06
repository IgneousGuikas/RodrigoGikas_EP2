import turtle
from random import shuffle
import unicodedata
import time


def nome_jogo(turtle):
    turtle.setpos(20,230)
    turtle.write('Jogo da Forca', font=('Arial',20,'bold'))
    turtle.home()

def desenho_forca(turtle, window_comprimento):
    coordenada_x1 = (window_comprimento/-2)+30
    turtle.setpos(coordenada_x1,-200)
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
    turtle.setpos(coordenada_x2,-200)
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
    turtle.setpos(coordenada_x,25)
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
    turtle.setpos(coordenada_x,-25)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(80)
    turtle.penup()
    turtle.left(90)
    turtle.home()

def desenho_left_arm(turtle, window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,-25)
    turtle.right(135)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.left(135)
    turtle.home()

def desenho_right_arm(turtle, window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,-25)
    turtle.right(45)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.left(45)
    turtle.home()

def desenho_left_leg(turtle, window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,-105)
    turtle.right(120)
    turtle.pendown()
    turtle.forward(65)
    turtle.penup()
    turtle.left(120)
    turtle.home()

def desenho_right_leg(turtle, window_comprimento):
    coordenada_x = (window_comprimento/-2)+205
    turtle.setpos(coordenada_x,-105)
    turtle.right(60)
    turtle.pendown()
    turtle.forward(65)
    turtle.penup()
    turtle.left(60)
    turtle.home()

def desenho_espacos(turtle, letras_palavra, window_comprimento):
    posicoes_letras = []
    coordenada_x = (window_comprimento/2)-30
    turtle.setpos(coordenada_x,-225)
    turtle.left(180)
    turtle.pensize(3)
    for i in letras_palavra:
        if i == ' ':
            turtle.forward(35)
            posicoes_letras.append([turtle.pos(),i])
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

def desenho_letras(turtle, palavra, posicoes_letras, escolha, window_comprimento, erros, acertos, erros_lista):
    text1 = str(unicodedata.normalize('NFKD',palavra).encode('ASCII','ignore'))
    no_accent = text1[2:len(text1)-1]
    
    coordenada_x = (window_comprimento/-2)+erros*20
    index_acertos = []
    erro = ''
    
    
    if escolha in no_accent:
        for x,e in enumerate(no_accent):
            if escolha == e:
                index_acertos.append(x)
        if index_acertos in acertos:
            None
        for i in index_acertos:
            turtle.setpos((posicoes_letras[i][0][0])+15,(posicoes_letras[i][0][1]))
            turtle.write(posicoes_letras[i][1], font=('Arial',20,'bold'))
            turtle.home()
        return 0,index_acertos,None
    else:
        erro = escolha
        if erro in erros_lista:
            return 1,None,None
        else:
            turtle.setpos(coordenada_x+30,-255)
            turtle.write(escolha, font=('Arial',18,'bold'))
            turtle.home()
            return 1,None,erro

def caneta_setup ():
    caneta.hideturtle()
    caneta.speed(100)
    caneta.penup()
    caneta.color('Black')
    caneta.pensize(5)

def setup_window(comprimento):
    if comprimento <= 500:
        comprimento += 80
        window.setup(width=comprimento,height=600,startx=None,starty=None)
    elif comprimento > 500 and comprimento <= 650:
        comprimento += 30
        window.setup(width=comprimento,height=600,startx=None,starty=None)
    elif comprimento > 650 and comprimento <= 800:
        comprimento -= 30
        window.setup(width=comprimento,height=600,startx=None,starty=None)
    elif comprimento > 800 and comprimento <= 1000:
        comprimento -= 110
        window.setup(width=comprimento,height=600,startx=None,starty=None)
    else:
        comprimento -= 250
        window.setup(width=comprimento,height=600,startx=None,starty=None)

def body_maker(erros):
    if erros == 1:
        desenho_cabeca(caneta, window.window_width())
    elif erros == 2:
        desenho_dorso(caneta, window.window_width())
    elif erros == 3:
        desenho_left_arm(caneta, window.window_width())
    elif erros == 4:
        desenho_right_arm(caneta, window.window_width())
    elif erros == 5:
        desenho_left_leg(caneta, window.window_width())
    elif erros == 6:
        desenho_right_leg(caneta, window.window_width())
        caneta.setpos(-100,100)
        caneta.write('Você perdeu', font=('Arial',18,'bold'))
        time.sleep(2)
        return True

def repor_desenho(turtle, posicoes_letras, acertos, erros, erros_lista, window_comprimento):
    coordenada_x = (window_comprimento/-2)+30
    
    for i in acertos:
        turtle.setpos((posicoes_letras[i][0][0])+15,(posicoes_letras[i][0][1]))
        turtle.write(posicoes_letras[i][1], font=('Arial',20,'bold'))
        turtle.home()
        
    if erros == 1:
        desenho_cabeca(caneta, window.window_width())
    elif erros == 2:
        desenho_cabeca(caneta, window.window_width())
        desenho_dorso(caneta, window.window_width())
    elif erros == 3:
        desenho_cabeca(caneta, window.window_width())
        desenho_dorso(caneta, window.window_width())
        desenho_left_arm(caneta, window.window_width())
    elif erros == 4:
        desenho_cabeca(caneta, window.window_width())
        desenho_dorso(caneta, window.window_width())
        desenho_left_arm(caneta, window.window_width())
        desenho_right_arm(caneta, window.window_width())
    elif erros == 5:
        desenho_cabeca(caneta, window.window_width())
        desenho_dorso(caneta, window.window_width())
        desenho_left_arm(caneta, window.window_width())
        desenho_right_arm(caneta, window.window_width())
        desenho_left_leg(caneta, window.window_width())
    elif erros == 6:
        desenho_cabeca(caneta, window.window_width())
        desenho_dorso(caneta, window.window_width())
        desenho_left_arm(caneta, window.window_width())
        desenho_right_arm(caneta, window.window_width())
        desenho_left_leg(caneta, window.window_width())
        desenho_right_leg(caneta, window.window_width())
        caneta.setpos(-100,100)
        caneta.write('Você perdeu', font=('Arial',18,'bold'))
        return True
    else:
        None
    
    turtle.setpos(coordenada_x,-255)
    for j in erros_lista:
        turtle.write(j, font=('Arial',18,'bold'))
        turtle.forward(20)

def sim():
    window.reset()
    caneta.setpos(-95,0)
    caneta.write('Clique para Sair', font=('Arial',18,'bold'))
    caneta.home()
    window.exitonclick()

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

while lista_palavras != []:
    shuffle(lista_palavras)
    palavra = lista_palavras[int(len(lista_palavras)/2)]
    del lista_palavras[int(len(lista_palavras)/2)]
    
    for i in palavra:
        letras_palavra.append(i)
    letras_palavra.reverse()
    
    comprimento = (len(letras_palavra)*35)*2

    setup_window(comprimento)
    nome_jogo(caneta)
    desenho_forca(caneta, window.window_width())
    
    posicoes_letras = desenho_espacos(caneta, letras_palavra, window.window_width())   
    
    escolha = ''
    erros = 0
    erros_lista = []
    acertos = []    
    
    while True:
        escolha = window.textinput('','Escolha uma letra ou chute a palavra')
        
        if escolha == None:
            caneta.setpos(-175,100)
            caneta.write('Jogador desistiu. Volte sempre.', font=('Arial',18,'bold'))
            time.sleep(2)
            break
        else:
            text1 = str(unicodedata.normalize('NFKD',palavra).encode('ASCII','ignore'))
            no_accent = text1[2:len(text1)-1]
            if escolha == no_accent or escolha == palavra:
                caneta.setpos(-100,100)
                caneta.write('Você ganhou', font=('Arial',18,'bold'))
                time.sleep(2)
                break
            elif escolha.isalpha() and len(escolha) == 1:
                a = []
                s = 0
                e = ''
                
                s,a,e = desenho_letras(caneta, palavra, posicoes_letras, escolha, window.window_width(), erros, acertos, erros_lista)
                if a == None:
                    a = []
                else:
                    for i in a:
                        acertos.append(i)
                        
                if e == None:
                    e = ''
                else:
                    erros_lista.append(e)
                    erros += s
                        
                
                p = body_maker(erros)
                if p == True:
                    break
                
                
                if len(acertos) == len(palavra):
                    caneta.setpos(-100,100)
                    caneta.write('Você ganhou', font=('Arial',18,'bold'))
                    time.sleep(2)
                    break
            else:
                caneta.setpos(-95,100)
                caneta.write('Escolha Inválida.', font=('Arial',18,'bold'))
                time.sleep(2)
                caneta.reset()
                caneta_setup()
                
                nome_jogo(caneta)
                desenho_forca(caneta, window.window_width())
                desenho_espacos(caneta, letras_palavra, window.window_width())
                repor_desenho(caneta, posicoes_letras, acertos, erros, erros_lista, window.window_width())
    caneta.reset()
    window.reset()
    caneta_setup()
    if escolha == None:
        caneta.setpos(-95,0)
        caneta.write('Clique para Sair', font=('Arial',18,'bold'))
        caneta.home()
        window.exitonclick()
   
        
    
    
'''
-------------------------------------------------------------------------------
'''



window.exitonclick()
