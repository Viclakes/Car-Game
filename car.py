from turtle import Screen
from car_player import Player
from car_manager import CarManager
from car_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Crossing Turtle")

player = Player()
c_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_right, "Right")
screen.onkey(player.go_left, "Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    c_manager.create_cars()
    c_manager.move_cars()

    # Detect collision with car
    for car in c_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.reset()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        c_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
