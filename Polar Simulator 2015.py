#Alistair Quinn
#Polar Simulator 2015 v2.0 - 25/10/2024
#Simple game were you shoot sprites and tally score 

#Imports and intitializes pygame module, sys for exiting game, and random to generate rand ints for spawning enemies
import pygame, sys, random
from pygame.locals import *
pygame.init()

#Class to create text objects to display text with no bg colour
class Text:
    def __init__(self):
        #Assigns parameters as instance variables
        self.font = pygame.font.SysFont("Impact", 72)
        self.text = ""
        self.colour = (255,0,0)
        self.x = 640
        self.y = 500
        #Creates and positions text surface and Rect object
        self.surface = self.font.render(self.text, True, self.colour)
        self.rect = self.surface.get_rect()
        self.rect.center = (self.x, self.y)

    #Draws a Text object to the screen
    def draw(self, screen):
        screen.blit(self.surface, self.rect)

    #Used to change displayed text of an instance and update Rect object with new dimensions
    def updateText(self, text):
        self.text = text
        self.surface = self.font.render(self.text, True, self.colour)
        self.rect = self.surface.get_rect(center = (self.x, self.y))
        self.rect.center = (self.x, self.y)

    #Checks if Text object has been clicked and returns a value if clicked or if not
    def clicked(self, events):
        #Loops thourgh events looking for mouse up, then checks if mouseclick collides with Text object
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                mouseClick = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouseClick):
                    return False
        return True

#Button class that inherits from Text. Only difference is bg colour specified 
class Button(Text):
    def __init__(self):
        Text.__init__(self)
        self.text = "START"
        self.y = 640
        self.surface = self.font.render(self.text, True, (0,0,0), (255,0,0))
        self.rect = self.surface.get_rect(center = (self.x, self.y))

#Player class used to create playable character on screen
class Player: 
    def __init__(self):
        #Scales sprite and crates right and left facing images, sets direction and updates Rec 
        self.rightImage = pygame.transform.smoothscale(pygame.image.load("assets/player.png"), (100, 200)).convert_alpha()
        self.leftImage = pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("assets/player.png"), (100, 200)), True, False).convert_alpha()
        self.image = self.leftImage
        self.facingLeft = True
        self.speed = 5
        self.x = 640
        self.y = 400
        self.rect = self.image.get_rect(center = (self.x, self.y))
        

    #Draws player to the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    #Used to detect WASD presses, and them move character on screen
    def move(self, key):
        if key[pygame.K_a]:
            self.facingLeft = True
            self.image = self.leftImage
            #If sprite isnt at edge of screen, decreses x to move sprite
            if self.x > 0:
                self.x = self.x - self.speed
                #Updates Rect with new position
                self.rect.center = (self.x, self.y)
        if key[pygame.K_d]:
            #Changes direction and sprite to right
            self.facingLeft = False
            self.image = self.rightImage
            #If sprite isnt at right edge of screen moves sprite
            if self.x < 1280:
                self.x = self.x + self.speed
                #Updates Rect to new position
                self.rect.center = (self.x, self.y)
        if key[pygame.K_w]:
            #Checks if y inst less than 100 or else prite would be drawn in water
            if self.y > 100:
                self.y = self.y - self.speed
                #Updates Rect with new y position
                self.rect.center = (self.x, self.y)
        if key[pygame.K_s]:
            #Checks to see if y is less than 520 or sprite would end up in 'water'
            if self.y < 520:
                self.y = self.y + self.speed 
                #Updates Rect with new y position
                self.rect.center = (self.x, self.y)


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


#Main Function that sets up game screen and runs each part of game            
def main():
    #Global fullscreen setting used throughout program to toggle fullscreen on and off
    global fullscreen
    fullscreen = True
    #Sets up game global screen
    global screen
    screen = pygame.display.set_mode((1280, 720), FULLSCREEN|DOUBLEBUF|HWSURFACE)
    #Sets up screen caption and icon
    caption = "Polar simulator 2015"
    pygame.display.set_caption(caption)
    pygame.display.set_icon(pygame.image.load("assets/player.png"))

    #Declaring Variables
    score = 0

    #Load main Music
    pygame.mixer.music.load("assets/music.ogg")
    pygame.mixer.music.play(-1)

    while True:
        #Displays start menu
        startMenu()
        #Runs game, stores returned score when completed
        score = game()
        #When the game is over, if user decides to play again true is returned and score is returned as 0
        gameOver(score)
        #If game hasn't ended, Resets Enemy class list
        Enemy.reset()


#Displays start menu to user
#When user clicks button, function ends 
def startMenu():
    startRunning = True
    #Sets up screen, running, background
    startBackground = pygame.image.load("assets/opening.jpg").convert()
    #Creates start button 
    introButton = Button()

    while startRunning:
        #Checks for events and stores them in local variables
        startEvents = pygame.event.get()
        startKey = pygame.key.get_pressed()

        #Draws background image
        screen.blit(startBackground, [0,0])

        #Draws start button to screen
        introButton.draw(screen)

        #Checks to see if start button clicked
        #If it is clicked, running set to false and next function will run
        startRunning = introButton.clicked(startEvents)

        #Checks for quit event
        Quit(startEvents)
        Fullscreen(startKey)

        #Updates display
        pygame.display.flip()


def game():
    #bool to turn while loop on and off
    gameRunning = True
    #Sets up background
    gameBackground = pygame.image.load("assets/background.jpg").convert()
    #Creates player object
    gamePlayer = Player()
    #Variable to keep track of score
    gameScore = 0
    #Creates clock object to limit FPS, time to hold calls to fpsClock.tick_busy_loop() to track game time
    gameFPSClock = pygame.time.Clock()
    gameTime = 0.00

    while gameRunning:
        #Draws background to screen
        screen.blit(gameBackground, [0,0])

        #Detects user input
        gameEvents = pygame.event.get()
        gameKey = pygame.key.get_pressed()

        #Draws Player and Detects Player Movement Key Press
        gamePlayer.move(gameKey)
        gamePlayer.draw(screen)

        #Generates Enemys and Tests for Player Collision
        Enemy.generate()
        Enemy.draw(screen)
        Enemy.move()
        gameRunning = Enemy.collide(gamePlayer.rect)

        #Generates Projectiles and Tests for Enemy hit detection
        Projectile.generate(gameKey, gamePlayer)
        Projectile.draw(screen)
        Projectile.move()
        gameScore += Projectile.collide()

        #Checks events
        Quit(gameEvents)
        Fullscreen(gameKey)

        #Updates display
        pygame.display.flip()

        #FPS setting
        gameTime = float(gameFPSClock.tick_busy_loop(60) / 1000.00)
        Enemy.time += gameTime
        Projectile.time += gameTime

    return gameScore

#Displays score to user and asks if they want to replay or quit
def gameOver(score):
    gameOverRunning = True
    #Variable set up
    gameOverBackground = pygame.image.load("assets/ending.jpg").convert()
    #Creates Score Text Object
    gameOverText = Text()
    #Updates score text to current score
    gameOverText.updateText(str(score))

    while gameOverRunning:
        #Draws background image
        screen.blit(gameOverBackground, [0,0])

        #Draws score to screen
        gameOverText.draw(screen)
        
        #Detect user input 
        gameOverEvents = pygame.event.get()
        gameOverKey = pygame.key.get_pressed()

        #Checks for quit event
        Quit(gameOverEvents)
        #Checks for key press, if spacebar restart game
        #If esc key game ends
        if gameOverKey[pygame.K_SPACE]:
            gameOverRunning = False
        elif gameOverKey[pygame.K_ESCAPE]:
            pygame.display.quit()
            sys.exit()
        #Toggles fullscreen
        Fullscreen(gameOverKey)
        
        #Updates display
        pygame.display.flip()

#Used to exit the game if x in pygame window is pressed
def Quit(events):
    for event in events:
        if event.type == QUIT:
            running = False
            pygame.display.quit()
            sys.exit()

#Used to make game fullscreen using F key
def Fullscreen(key):
    if key[K_f]:
        #Tells python we mean the global fullscreen not a new local
        global fullscreen
        fullscreen = not fullscreen
        if fullscreen:
            pygame.display.set_mode((1280, 720), FULLSCREEN|DOUBLEBUF|HWSURFACE)
        else:
            pygame.display.set_mode((1280, 720), DOUBLEBUF|HWSURFACE)

main()
