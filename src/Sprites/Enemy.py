import pygame
import random

#Enemy class used to create enemies in the game
class Enemy: 
    #List to hold new Enemys that are created. Objects get appended here when initialised 
    List = []
    #Bool used to alternate spawning of Enemyes. When True Enemy will spawn on left side of screen
    #Bool is then switched to False and next Enemy will spawn on right side ect.
    isLeft = True
    #Holds spawnRate of Enemy class
    spawnRate = 1.00
    #Used to keep track of time for events
    time = 0.00
    #Death sound
    death = pygame.mixer.Sound("assets/death.ogg")

    def __init__(self):
        #If isLeft True, Creates sprite on left side of screen 
        if Enemy.isLeft:
            self.image = pygame.transform.smoothscale(pygame.image.load("assets/Explorer.png"), (100, 200)).convert_alpha()
            self.x = 0
            self.y = random.randint(100, 720 - 200)
            self.facingLeft = False
            Enemy.isLeft = not Enemy.isLeft
        else: 
            #Flips and scales sprite image to face left
            self.image = pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("assets/Explorer.png"), (100, 200)), True, False).convert_alpha()
            self.x = 1280
            self.y = random.randint(100, 720 - 200)
            self.facingLeft = True
            Enemy.isLeft = not Enemy.isLeft

        #Generates a random float between 0.1 and 5.0 inclusive
        self.speed = random.uniform(0.1, 5.0)

        #Creates Rect object and positions sprite
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        #Appends new Object to Class List to be used later
        Enemy.List.append(self)

    #Generates Enemys at a determined spawn rate appends them to Class List
    @classmethod
    def generate(Class):
        if Class.time > Class.spawnRate:
            Class.List.append(Enemy())
            Class.time = 0

    #Blits all the objects in Class List to the screen
    @classmethod
    def draw(Class, screen):
        for i in Class.List:
            screen.blit(i.image, i.rect)

    #Makes all the objects in the Class List move on their own
    @classmethod
    def move(Class):
        for i in Class.List:
            if i.facingLeft == False:
                i.x = i.x + i.speed
                i.rect.center = (i.x, i.y)
                #Removes object once it gets to end of screeen
                if i.x > 1280:
                    Class.List.remove(i)
            else:
                i.x = i.x - i.speed
                i.rect.center = (i.x, i.y)
                if i.x < 0:
                    Class.List.remove(i)

    #Checks if any object in the Class List has collided with the Player Rect
    @classmethod
    def collide(Class, playerRect):
        for i in Class.List:
            if i.rect.colliderect(playerRect):
                return False
        return True

    #Empties Class List, used when game needs to be restarted fresh
    @classmethod
    def reset(Class):
        for i in Class.List:
            Class.List.remove(i)
        Class.List = []