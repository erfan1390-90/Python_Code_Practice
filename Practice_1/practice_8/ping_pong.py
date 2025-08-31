import pygame
pygame.init()
class Color:
    black=(0,0,0)
    white=(255,255,255)
    yelow=(255,255,0)
    blue=(0,0,255)
    red=(255,0,0)
class Ball:
    def __init__(self):
        self.r=10
        self.x=Game.width/2
        self.y=Game.height/2
        self.speed=2
        self.color=Color.yelow
        self.x_direction=+1
        self.y_direction=-1
        self.area=pygame.draw.circle(Game.screen,self.color,[self.x,self.y],self.r)
    def show(self):
        self.area=pygame.draw.circle(Game.screen,self.color,[self.x,self.y],self.r)
    def move(self):
        self.x+=self.speed*self.x_direction
        self.y+=self.speed*self.y_direction

        if self.y > Game.height - self.r or self.y < self.r:
            self.y_direction *= -1

    def new(self):
        self.x=Game.width/2
        self.y=Game.height/2

class Racket:
    def __init__(self,x,y,color):
        self.color=color
        self.h=50
        self.w=10
        self.speed=2
        self.score=0
        self.x=x
        self.y=y
        #self.area=pygame.draw.rect(Game.screen,self.color,[self.x,self.y,self.w,self.h])
    def show(self):
        self.area=pygame.draw.rect(Game.screen,self.color,[self.x,self.y,self.w,self.h])
        return self.area
    def move(self,b):
        if self.y<b.y:
            self.y+=self.speed
        elif self.y>b.y:
            self.y-=self.speed
        if self.y<0:
            self.y=0
        if self.y>Game.height - self.h:
            self.y=Game.height-self.h


class Game:

    width=400
    height=300
    color=(255,255,255)
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption('ping-pong')

    clock=pygame.time.Clock()
    fps=120
    font=pygame.font.SysFont("arial",16)
    @staticmethod
    def play():
        ball=Ball()
        me=Racket(0,Game.height/2,Color.red)
        computer=Racket(390,Game.height/2,Color.blue)
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()
                if event.type==pygame.MOUSEMOTION:
                    me.y=pygame.mouse.get_pos()[1]
                    if me.y>Game.height-me.h:
                        me.y=Game.height-me.h


            ball.move() 
            computer.move(ball)

            if ball.x<0:
                computer.score+=1
                # print(10*"*")
                # print(f"your score:{me.score}")
                # print(f"computer score:{computer.score}")
                # print(10*"*")
                ball.new()
            elif ball.x>Game.width:
                me.score+=1
                # print(10*"*")
                # print(f"your score:{me.score}")
                # print(f"computer score:{computer.score}")
                # print(10*"*")

                ball.new()
            if computer.score==11:
                print(10*"*")
                print("Game Over")
                print(10*"*")
                exit()
            if me.score==11:
                print(10*"*")
                print("Game Win")
                print(10*"*")
                exit()
            if me.show().colliderect(ball.area) :
                ball.x_direction =+1

            elif computer.show().colliderect(ball.area):
                ball.x_direction =-1

            Game.screen.fill((0,255,50))
            pygame.draw.rect(Game.screen,Game.color,[0,0,Game.width,Game.height],10)
            pygame.draw.aaline(Game.screen,Game.color,[Game.width/2,0],[Game.width/2,Game.height])
            me_score=Game.font.render(f"your score:{me.score}",True,Color.red)
            computer_score=Game.font.render(f"computer score:{computer.score}",True,Color.red)
            Game.screen.blit(me_score, (10,10))
            Game.screen.blit(computer_score,(Game.width-110,10))
            ball.show()
            me.show()
            computer.show()
            pygame.display.update()
            Game.clock.tick(Game.fps)
if __name__ =="__main__":
    Game.play()