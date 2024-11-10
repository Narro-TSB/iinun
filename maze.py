#создай игру "Лабиринт"!
from pygame import *


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



class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.player_speed
        if keys_pressed[K_s] and self.rect.y <= 435:
            self.rect.y += self.player_speed
        if keys_pressed[K_d] and self.rect.x <= 635:
            self.rect.x += self.player_speed
        if keys_pressed[K_a] and self.rect.x >= 0:
            self.rect.x -= self.player_speed

        

class Enemy(GameSprite):
    def update(self):
        if self.rect.x >= 630:
            self.direction = 'left'
            
        if self.rect.x <= 350:
            self.direction = 'right'
            
        if self.direction == 'left':
            self.rect.x -= self.player_speed
        else:
            self.rect.x += self.player_speed

class Wall(sprite.Sprite):
    def __init__(self, hight_wall, wight_wall, rect_x, rect_y):
        super().__init__()
        self.hight_wall = hight_wall
        self.wight_wall = wight_wall
        self.image = Surface((wight_wall, hight_wall))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

font.init()
font = font.SysFont("Arial", 70)
win = font.render(
    'YOU WIN!', True, (255,215,0)
)
GAMEOVER = font.render(
    'YOU LOSER!', True, (160,0,0)
)



mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
window = display.set_mode((700,500))
background = transform.scale(image.load('background.jpg'),(700,500))
window.blit(background,(0,0))
clock = time.Clock()
x1 = 100
x2 = 400
y1 = 400
y2 = 400
x3=535
y3=100

wall1 = Wall(300, 20, 100, 50)
wall2 = Wall(20, 400, 0, 50)
wall3 = Wall(400, 20, 250, 150)
wall4 = Wall(300, 20, 400, 50)
walls=[wall1,wall2,wall3,wall4]

hero1=Player('hero.png',x1,y1,4)


cyborg=Enemy('cyborg.png',x2,y2,4)

money = Enemy('treasure.png', x3,y3,0)

finish = False


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        for w1 in walls:
            w1.draw_wall()
        for w1 in walls:
            if sprite.collide_rect(hero1, w1):
                finish=True
                window.blit(GAMEOVER,(250,100))
        if sprite.collide_rect(hero1, cyborg):
            finish=True
            window.blit(GAMEOVER,(250,100))
            
        if sprite.collide_rect(hero1, money):
            finish=True
            window.blit(win,(250,100))
        money.update()
        hero1.update()
        cyborg.update()
        money.reset()
        hero1.reset()
        cyborg.reset()
        
    
    display.update()
    clock.tick(60)
