import turtle

#entorno grafico
screen=turtle.Screen()
screen.title("Aspiradora Agente")
screen.bgcolor("black")
screen.setup(width=900,  height=900)
screen.tracer(0)

#aspiradora punto
asp=turtle.Turtle()
asp.speed(0)
asp.shape("square")
asp.color("white")
asp.penup() #no deja rastro de lo que avanza
asp.goto(0,0)
asp.direction="stop" #se queda quieto a un inicio

#fun para moverse

while True:
    screen.update()
