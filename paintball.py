from pygame import *


#Class
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.player_image = transform.scale(image.load(player_image),(65,65))
        self.rect = self.player_image.get_rect()
        self.player_speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = ''
    def reset(self):
        window.blit(self.player_image, (self.rect.x, self.rect.y))
#--------------------------------------------------
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.player_speed
        if keys_pressed[K_s] and self.rect.y <= 435:
            self.rect.y += self.player_speed
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.player_speed
        if keys_pressed[K_DOWN] and self.rect.y <= 435:
            self.rect.y += self.player_speed
#--------------------------------------------------
class Ball(GameSprite):
    def Gameover(self):
        global finish
        if self.rect.x >= 620:
            finish = False

        if self.rect.x <= 20:
            finish = False
            
        if self.rect.y >= 500:
            finish = False
    def update(self):
            self.rect.x += self.player_speed
        
#--------------------------------------------------
window = display.set_mode((700,500))
background = transform.scale(image.load("background.png"),(700,500))
window.blit(background,(0,0))
#--------------------------------------------------
clock = time.Clock()
#--------------------------------------------------
game = True
finish = False
#--------------------------------------------------
#Players
Player_1 = Player('platform.png', 20, 250, 3)
Player_2 = Player('platform.png', 620, 250, 3)
#Enemy
ball = Ball('painball_ball.png', 350, 250, 2)
#--------------------------------------------------
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        #Blit sprites
        Player_1.update()
        Player_2.update1()
        Player_1.reset()
        Player_2.reset()
        ball.update()
        ball.reset()

        if sprite.collide_rect(Player_1, ball):
            ball.player_speed *= -1
        if sprite.collide_rect(Player_2, ball):
            ball.player_speed *= -1
        if ball.rect.y >= 500:
            ball.player_speed *= -1
        if ball.rect.y <= 0:
            ball.player_speed *= -1
        if ball.rect.x >= 620:
            game = False
        if ball.rect.x <= 0:
            game = False

    display.update()
    clock.tick(60)
#--------------------------------------------------