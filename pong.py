import turtle

# Konfiguracja okna
win = turtle.Screen()
win.title("Pong w Pythonie!")
win.bgcolor("#1a1a2e")  # ciemny granatowy kolor tła
win.setup(width=800, height=600)
win.tracer(0)

# Delikatne paski tła (imitacja gradientu)
stripe = turtle.Turtle()
stripe.speed(0)
stripe.color("#16213e")
stripe.penup()
stripe.hideturtle()
for y in range(-300, 300, 30):
    stripe.goto(-400, y)
    stripe.begin_fill()
    for _ in range(2):
        stripe.forward(800)
        stripe.left(90)
        stripe.forward(15)
        stripe.left(90)
    stripe.end_fill()

# Lewa paletka – niebieska
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("#3a6ea5")  # jaśniejszy niebieski
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Prawa paletka – czerwona
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("#e94560")  # czerwony róż
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Piłka – jasnoszara
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("#c7d3dd")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Wynik
score_left = 0
score_right = 0

# Pen do wyświetlania wyniku
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)

def update_score():
    score_pen.clear()
    score_pen.write(f"Gracz A: {score_left}    Gracz B: {score_right}", align="center",
                    font=("Courier", 24, "bold"))

update_score()

# Ruch paletek
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        left_paddle.sety(y + 30)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -240:
        left_paddle.sety(y - 30)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        right_paddle.sety(y + 30)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -240:
        right_paddle.sety(y - 30)

# Sterowanie
win.listen()
win.onkeypress(left_paddle_up, "w")
win.onkeypress(left_paddle_down, "s")
win.onkeypress(right_paddle_up, "Up")
win.onkeypress(right_paddle_down, "Down")

# Pętla gry
while True:
    win.update()

    # Ruch piłki
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Odbijanie piłki od ścian
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Odbijanie piłki od paletek
    if (ball.xcor() > 340 and ball.xcor() < 350 and
            (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50)):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350 and
            (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50)):
        ball.setx(-340)
        ball.dx *= -1

    # Punktacja: piłka poza ekranem
    if ball.xcor() > 390:
        score_left += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_right += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1
