import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
car_manager = CarManager()
player=Player()
scoreboard=Scoreboard()
def go_up():
    player.move_forward()

screen.listen()
screen.onkey(go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(car_manager.car_speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) <20:
            game_is_on=False
            scoreboard.game_over()
    if player.ycor()>280:
        car_manager.car_speed*=0.5
        scoreboard.display_score()
        player.original_position()


screen.exitonclick()

