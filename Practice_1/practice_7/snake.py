import pygame
import random
pygame.init()
class Frute:
    def __init__(self):
        self.r=10
        self.height=390
        self.width=590
        self.x=random.randint(10,self.width)
        self.y=random.randint(10,self.height)
        self.color=(0,0,0)
    def show(self):
        pygame.draw.circle(output.display,self.color,[self.x,self.y],self.r)
        
class Apple(Frute):
    def __init__(self):
        Frute.__init__(self)
        self.color=(255,0,0)
class Golden_Apple(Frute):
    def __init__(self):
        Frute.__init__(self)
        self.color=(255,255,0)
class Kharab_Apple(Frute):
    def __init__(self):
        Frute.__init__(self)
        self.color=(1,1,1)
class Snake:
    def __init__(self):
        self.w=16
        self.h=16
        self.width=600
        self.height=400
        self.display=pygame.display.set_mode((self.width, self.height))
        self.clock=pygame.time.Clock()
        self.x=self.width/2
        self.color=(0,127,7)
        self.color2=(21,196,89)
        self.y=self.height/2
        self.name= "python"
        self.speed=18
        self.score=0   
        self.body=[]
        self.x_change=0
        self.y_change=0

    def show(self):
        pygame.draw.rect(self.display,self.color,[self.x,self.y,self.w,self.h])
        # self.body.append({"x":self.x,"y":self.y})
        # if len(self.body)>self.score:
        #     self.body.remove(self.body[0])
        for item in self.body:
            pygame.draw.rect(self.display,self.color2,[item["x"],item['y'],self.w,self.h])
    def move(self):
        # self.body.append({"x":self.x,"y":self.y})
        # if len(self.body)>self.score:
        #     self.body.remove(self.body[0])

        if self.x_change==-1:
            self.x-=self.speed
        elif self.x_change==1:
            self.x+=self.speed
        elif self.y_change==-1:
            self.y-=self.speed
        elif self.y_change==1:
            self.y+=self.speed

    def score_m(self):

        if (self.x >= apple.x - apple.r - 7 and self.x <= apple.x + apple.r + 7) and (self.y >= apple.y - apple.r - 7 and self.y <= apple.y + apple.r + 7):
            self.score+=1
            #print(f"score:{self.score}")
            apple.x = random.randint(10, apple.width-10 )
            apple.y = random.randint(10, apple.height-10 )
        if (self.x >= G_apple.x - G_apple.r - 7 and self.x <= G_apple.x + G_apple.r + 7) and (self.y >= G_apple.y - G_apple.r - 7 and self.y <= G_apple.y + G_apple.r + 7):
            self.score+=2
            #print(f"score:{self.score}")
            G_apple.x = random.randint(10, apple.width-10 )
            G_apple.y = random.randint(10, apple.height-10 )
        if (self.x >= k_apple.x - k_apple.r - 7 and self.x <= k_apple.x + k_apple.r + 7) and (self.y >= k_apple.y - k_apple.r - 7 and self.y <= k_apple.y + k_apple.r + 7):
            if self.score>0:
                self.score-=1
                if self.score<len(self.body):
                    self.body.remove(self.body[0])
            #print(f"score:{self.score}")
            k_apple.x = random.randint(10, apple.width-10 )
            k_apple.y = random.randint(10, apple.height-10 )
        self.body.append({"x":self.x,"y":self.y})
        if len(self.body)>self.score:
             self.body.remove(self.body[0])
        
        if output.x < 0 or output.x > 590 or output.y < 0 or output.y > 390:
                    print("*"*10)
                    print("Game Over")
                    print("*"*10)
                    self.score=0
                    self.x=self.width/2
                    self.y=self.height/2
                    self.x_change=0
                    self.y_change=0
                    self.h=16
                    self.body.clear()
                    #exit()
        if self.score==250:
            print("*"*10)
            print("Game Win")
            print("*"*10)
            exit()

if __name__=="__main__":
    output=Snake()
    apple=Apple()
    G_apple=Golden_Apple()
    k_apple=Kharab_Apple()
    font=pygame.font.SysFont("Arial",32)
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                print("Good bye")
                exit()

            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    output.y_change=-1
                    output.x_change=0
                if event.key == pygame.K_DOWN:
                    output.y_change=1
                    output.x_change=0
                if event.key == pygame.K_LEFT:
                    output.x_change=-1
                    output.y_change=0
                if event.key == pygame.K_RIGHT:
                    output.x_change=1
                    output.y_change=0
                if event.key == pygame.K_b:
                    exit()
                if event.key == pygame.K_s:
                    print(f"your score:{output.score}")
                if event.key==pygame.K_p:
                        output.x_change=0
                        output.y_change=0

        output.move()
        # result=output.score_m()
        # if result ==True:
        #     output.Apple()
        color=(255,255,0)
        score_screen=font.render(f"your score:{output.score}",True,color)
        output.display.blit(score_screen,(10,10))

        output.display.fill((0,0,255))
        output.display.blit(score_screen,(10,10))
        output.show()
        G_apple.show()
        k_apple.show()
        apple.show()
        output.score_m()
        pygame.display.update()
        output.clock.tick(8)
