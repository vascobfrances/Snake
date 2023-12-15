import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen= Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)< 15: #VERIFCAR DISTANCIA PARA A COMIDA
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 285  or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285: #verificar colisões com parede
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]: #verificar colisão com cauda
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)< 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()