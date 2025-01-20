import pgzrun
from random import randint

WIDTH=700
HEIGHT= 600
TITLE= "FLAPPY BIRD BALL"

R=randint(0, 255)
G=randint(0, 255)
B=randint(0, 255)
color=R,G,B

GRAVITY=2000

class Ball:
    def __init__(self, initial_X, initial_Y):
        self.x= initial_X
        self.y= initial_Y
        self.vx=200
        self.vy=0
        self.radius=30
    def draw(self):
        pos=(self.x, self.y)
        screen.draw.filled_circle(pos,self.radius,color)

ball=Ball(0, 50)

def draw():
    screen.clear()
    ball.draw()
def update(dt):
    #apply constant acceleration formule
    uy=ball.vy       #uy is the initial velocity, vy is the final velocity
    ball.vy += GRAVITY *dt
    ball.y += (uy +ball.vy)* 0.5 *dt

    #detect and handle bounce
    if ball.y > HEIGHT - ball.radius:    #we've bounced!
        ball.y= HEIGHT-ball.radius       #fix the position
        ball.vy = -ball.vy * 0.9         #inelastic collision

    #X component doesn't have acceleration
    ball.x += ball.vx * dt
    if ball.x > WIDTH -ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = -500 

pgzrun.go()
    



