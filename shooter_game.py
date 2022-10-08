#Создай собственный Шутер!

from pygame import *
from random import *
class Game_sprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
window = display.set_mode((900,600))
display.set_caption("Шутер")


font.init()
font = font.Font(None, 36)


win = font.render("YOU WON", True, (255, 215, 0))
lose = font.render("А уже всё, ты слил, GG", True, (155, 255, 0))

class Player(Game_sprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 810:
            self.rect.x += self.speed    
    def fire(self):
        bulet = bullet("bullet.png",self.rect.centerx,self.rect.top,10,15,20)
        bullets.add(bulet)
lol = 0
tablo = 0
gg = 0
class Enemy(Game_sprite):
    def update(self):
        self.rect.y += self.speed
        global  lol
        if self.rect.y > 600:
            self.rect.y = 0
            self.rect.x = randint(50,850)
            lol +=1
    '''def update(self):
        self.rect.y += self.speed
        global gg
        if self.rect.y > 600:
            self.rect.y = 0
            self.x = randint(50, 850)
            gg +=1'''


class bullet(Game_sprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()



background =  transform.scale(image.load("galaxy.jpg"),(900,600))
sprite1 =  Player("rocket.png",450,490,15,95,115)
monsters = sprite.Group()
for i in range(1,6):
    monstr = Enemy("ufo.png",randint(50,850),30,randint(3,5),110,100)
    monsters.add(monstr)
stars = sprite.Group()
for i in range(1,2):
    star = Enemy("asteroid.png",randint(50,850),30,randint(1,2),150,150)
    stars.add(star)
bullets = sprite.Group()





mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()



finish = False

game = True
Clock = time.Clock()
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                sprite1.fire() 

    if  finish != True:
        window.blit(background,(0,0))
        tab = font.render("Пропущено:"+ str(lol),1,(65,173,0))
        window.blit(tab,(0,0))
        tab2 = font.render("Счёт:"+ str(tablo),1,(65,173,0))
        window.blit(tab2,(0,25))
        tab3 = font.render("Астероидов:"+ str(gg),1,(65,173,0))
        window.blit(tab3,(0,50))
        sprite1.update()
        bullets.update()
        star.update()
        monsters.update()
        monsters.draw(window)
        stars.draw(window)
        sprite1.reset()
        bullets.draw(window)
        
        if sprite.spritecollide(sprite1, monsters,False) or lol >= 10:
            finish = True
            window.blit(lose,(400,250))
        

        boom = sprite.groupcollide(monsters, bullets, True,True)
        for i in boom:
            tablo = tablo + 1
            monstr = Enemy("ufo.png",randint(50,850),30,randint(3,5),110,110)
            monsters.add(monstr)
        if tablo >= 101:
            finish = True
            window.blit(win,(450,300))

        boom2 = sprite.groupcollide(stars, bullets, True, True)
        for i in boom2:
            gg = gg + 1
            star = Enemy("asteroid.png",randint(50,850),30,randint(1,2),150,150)
            stars.add(star)
        if gg >= 15:
            finish = True
            window.blit(lose(450,300))


    display.update()
    time.delay(10)
































