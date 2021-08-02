import turtle
import time
import random

timee=0.15

#marcador
score=0
high_score=0

#entorno grafico
screen=turtle.Screen()
screen.title("Aspiradora Agente")
screen.bgcolor("black")
screen.setup(width=600,  height=600)
screen.tracer(0)

#aspiradora punto
asp=turtle.Turtle()
asp.speed(0)
asp.shape("square")
asp.color("white")
asp.penup() #no deja rastro de lo que avanza
asp.goto(0,0)
asp.direction="stop" #para que inicie en stop, luego sigue moviendose

#garbage punto
gar=turtle.Turtle()
gar.speed(0)
gar.shape("circle")
gar.color("yellow")
gar.penup() #no deja rastro de lo que avanza
gar.goto(0,100)

#cuerpo
#cuerpo=[]

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0        High Score: 0", align="center", font=("Courier", 12, "normal"))

#movimientos tecla
def arriba():
    asp.direction="up"
def abajo():
    asp.direction="down"
def izquierda():
    asp.direction="left"
def derecha():
    asp.direction="right"

#movimientos apiradora
def movimiento():
    if asp.direction=="up": #arriba
        y= asp.ycor() #se obtiene coordenada en y 
        asp.sety(y+20) #actualizo valor y se mueve 20p

    if asp.direction=="down": #abajo
        y= asp.ycor() #se obtiene coordenada en y
        asp.sety(y-20)
    
    if asp.direction=="left": #izquierda
        x= asp.xcor() #se obtiene coordenada en x
        asp.setx(x-20)

    if asp.direction=="right": #derecha
        x= asp.xcor() #se obtiene coordenada en x
        asp.setx(x+20)

#teclado
screen.listen()
screen.onkeypress(arriba,"Up")
screen.onkeypress(abajo,"Down")
screen.onkeypress(izquierda,"Left")
screen.onkeypress(derecha,"Right")

while True:
    screen.update()

    #colision borde (marco ventana)
    if asp.xcor() > 280 or asp.xcor() < -280 or asp.ycor() > 210 or asp.ycor() < -280:
        #time.sleep(1)
        asp.goto(0,0)
        asp.direction = "right"
        # for segmento in cuerpo:
        #     segmento.hideturtle()

        #cuerpo.clear() #limpia lista de segmentos

        score = 0 
        texto.clear()
        texto.write("Score: {}        High Score: {}".format(score,high_score)
        , align="center", font=("Courier", 12, "normal"))
        
    #colisiones comida
    if asp.distance(gar) < 20: #20 por tamanio pix
        x=random.randint(-280,280)
        y=random.randint(-280,210)
        gar.goto(x,y)#si pasa encima (aspira) se mueve random
        
        # cuerpo_cua=turtle.Turtle()
        # cuerpo_cua.speed(0)
        # cuerpo_cua.shape("square")
        # cuerpo_cua.color("grey")
        # cuerpo_cua.penup()
        # cuerpo.append(cuerpo_cua)

        score +=10
        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}        High Score: {}".format(score,high_score)
        , align="center", font=("Courier", 12, "normal"))


    #cuerpo se mueve
    # longcuerpo=len(cuerpo)
    # for i in range(longcuerpo -1,0,-1): #primer -1 por el indice 
    #     x= cuerpo[i-1].xcor()
    #     y= cuerpo[i-1].ycor()
    #     cuerpo[i].goto(x,y) #cuerpo actual se mueve con el index en esas coordenadas
    # if longcuerpo > 0: #hay elementos en la cabeza
    #     x=asp.xcor()
    #     y=asp.ycor()
    #     cuerpo[0].goto(x,y) 

    movimiento()
    time.sleep(timee)