import turtle
import random

screen = turtle.Screen()

screen.bgcolor("light blue")
screen.title("catch the Turtle game")
FONT = ('Arrial', '25', 'normal')





# turtle list
turtle_list=[]



countdown_turtle=turtle.Turtle()


turtle_list=[]
x_coordinates=[-30,-20,-10,0,10,20,30]
y_coordinates=[-20,-10,0,10,20]
grid_size=10
score=0
game_over=False

score_turtle = turtle.Turtle()
score_turtle.color("dark blue")
screen_size = screen.window_height()
score_turtle.penup()
score_turtle.goto(0, screen_size / 2 * 0.85)
score_turtle.write(arg="Score:0", move=False, align="center", font=FONT)
score_turtle.hideturtle()


def make_turtle(x,y):
    green_turtle = turtle.Turtle()

    def handle_click(x,y):
        global score
        score+=1

        score_turtle.clear()
        score_turtle.write(arg="Score:{}".format(score), move=False, align="center", font=FONT)

    green_turtle.onclick(handle_click)
    green_turtle.shapesize(2, 2)
    green_turtle.shape("turtle")
    green_turtle.color("red")

    green_turtle.penup()
    green_turtle.goto(x * grid_size, y * grid_size)
    turtle_list.append(green_turtle)


def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
           make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()
def show_turtle_randomly():
    if not game_over:

        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtle_randomly,1000)  #recersve fun : kendi içinde çalıştırıyoruz




def countdown_timer(time):
    global game_over


    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    screen_size = screen.window_height()
    countdown_turtle.penup()
    countdown_turtle.goto(0, screen_size / 2 * 0.75)
    countdown_turtle.write(arg="Time:{}".format(time), move=False, align="center", font=FONT)
    countdown_turtle.clear()

    if time >0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time:{}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda :countdown_timer(time-1),1200)


    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!!!", move=False, align="center", font=FONT)

        gif_turtle = turtle.Turtle()
        gif_turtle.hideturtle()


        if score>5 :

            gif_turtle.color("red")
            gif_turtle.write(arg="Tebrikler oyunu kazandınız :))", move=False, align="center", font=FONT)
        else:
            gif_turtle.write(arg="Oyunu Kaybettiniz :((", move=False, align="center", font=FONT)




def game_startup():
    turtle.tracer(0)  #taki etmeyi bırakıyoruz

    setup_turtles()
    hide_turtles()
    show_turtle_randomly()

    turtle.tracer(1)   #takit etmeye başlıyoruz
    countdown_timer(10)

game_startup()














turtle.mainloop()