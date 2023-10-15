from pygame import *

font.init()
font = font.Font(None,50)

img_back = "blue.jpg" 
img_hero = "ball.jpg"
img_ball = 'pngwing.com.png'  

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        
        sprite.Sprite.__init__(self)

       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

      
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):

    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def update_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

clock = time.Clock()
win_width = 700
win_height = 500
display.set_caption("Ping Pong!")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('blue.jpg'), (win_width, win_height))

ship_1 = Player(img_hero, 665, 130, 30, 100, 10)
ship_2 = Player(img_hero, 5, 130, 30, 100, 10)
ball = Player(img_ball, 300, 130, 90, 100, 10)
lose_1 = font.render('Первый проиграл!',True,(255,215,0))
lose_2 = font.render('Второй проиграл!',True,(180,0,0))
ball_x = 5
ball_y = 5

finish = False

run = True 
while run:
    
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
      
        window.blit(background,(0,0))
        
        ship_1.reset()
        ship_1.update_1()

        ship_2.reset()
        ship_2.update_2()

        ball.reset()
        ball.rect.x += ball_x
        ball.rect.y += ball_y
        
        if sprite.collide_rect(ship_1,ball) or sprite.collide_rect(ship_2,ball):
            ball_x *= -1
            ball_y *= 1
        if ball.rect.y < 0 or ball.rect.y > 450:
            ball_y *= -1
        if ball.rect.x < -40:
            finish = True
            window.blit(lose_1,(200,200))
        if ball.rect.x > 650:
            finish = True
            window.blit(lose_2,(200,200))


        display.update()
    
        time.delay(50)