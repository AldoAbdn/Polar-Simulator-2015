import pygame
import Enemy

#Projectile Class to create Projectiles that are fired at Enemys
class Projectile():
    #Class variable List that stores new instances of Projectile objects
    List = []
    #Loads sounds
    sound = pygame.mixer.Sound("assets/shot.ogg")
    soundReload = pygame.mixer.Sound("assets/gunReload.ogg")
    #Time counter used to limit how often players can shoot 
    time = 0.00
    #Defines reload time
    reloadTime = 1.00

    def __init__(self, player):
        self.image = pygame.transform.smoothscale(pygame.image.load("assets/Bullet.png"), (12, 12)).convert()
       
        #Spawns projectiles on correct side of player
        if player.facingLeft:
            self.x = player.x - 55
            self.y = player.y + 10
            self.facingLeft = True
        else: 
            self.x = player.x + 55
            self.y = player.y + 10
            self.facingLeft = False

        #Sets speed of Projectiles
        self.speed = 10

        #Sets Rect object
        self.rect = self.image.get_rect(center = (self.x, self.y))

        #Appends each new instance to Class List
        Projectile.List.append(self)
        
    #Checks for spacebar press in list returned by pygame.key.get_pressed()    
    @classmethod
    def generate(Class, key, player):
        if key[pygame.K_e]:
            if Class.time > Class.reloadTime:
                Class.sound.play()
                Class.soundReload.play()
                Class.List.append(Projectile(player))
                Class.time = 0
     
    #Draws Class List to the screen           
    @classmethod
    def draw(Class, screen):
        for i in Class.List:
            screen.blit(i.image, i.rect)

    #Moves objects in class list across screen. Speed determined by instance variable value .speed
    @classmethod
    def move(Class):
        for i in Class.List:
            if not i.facingLeft and i.x <= 1280:
                i.x = i.x + i.speed
                i.rect.center = (i.x, i.y)
            elif i.facingLeft and i.x >= 0:
                i.x = i.x - i.speed
                i.rect.center = (i.x, i.y)

    #Checks if any Projectiles in class list hit any Enemys in Enemy class list
    @classmethod
    def collide(Class):
        for i in Class.List:
            for j in Enemy.List:
                if i.rect.colliderect(j.rect):
                    Enemy.death.play()
                    Class.List.remove(i)
                    Enemy.List.remove(j)
                    return 50
                elif i.x <= 0 or i.x >= 1280:
                    Class.List.remove(i)
                    return 0
        return 0