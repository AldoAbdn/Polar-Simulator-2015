import pygame, sys
from Sprites import Enemy
from UI import Button
from pygame.locals import *
pygame.init()

class Game:
    def __init__(self, fullscreen=True, fps=60) -> None:
        self.fullscreen = fullscreen
        self.surface = pygame.display.set_mode((1280, 720), FULLSCREEN|DOUBLEBUF|HWSURFACE)
        #Sets up screen caption and icon
        self.caption = "Polar simulator 2015"
        pygame.display.set_caption(self.caption)
        pygame.display.set_icon(pygame.image.load("assets/player.png"))
        #Declaring Variables
        self.score = 0
        self.fpsClock = pygame.time.Clock()
        self.time = 0.00
        self.fps = fps
        #Load main Music
        pygame.mixer.music.load("assets/music.ogg")
        pygame.mixer.music.play(-1)

    #Runs game loop            
    def run(self):
        while True:
            #Displays start menu
            self.startMenu()
            #Runs game, stores returned score when completed
            score = self.game()
            #When the game is over, if user decides to play again true is returned and score is returned as 0
            self.gameOver(score)
            #If game hasn't ended, Resets Enemy class list
            Enemy.reset()

    def runScreen(self, screen):
        while screen.running:
            #Checks for events and stores them in local variables
            self.handleEvents()
            self.handleKeyPresses()
            #Blit to Screen
            screen.run(self.surface)
            #FPS
            self.time = float(self.fpsClock.Clock.tick_busy_loop(self.fps) / 1000.00)



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
    def handleEvents(self):
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                running = False
                pygame.display.quit()
                sys.exit()

    #Used to make game fullscreen using F key
    def handleKeyPresses(self, key):
        keys = pygame.key.get_pressed()
        if key[K_f]:
            #Tells python we mean the global fullscreen not a new local
            self.fullscreen = not self.fullscreen
            if self.fullscreen:
                pygame.display.set_mode((1280, 720), FULLSCREEN|DOUBLEBUF|HWSURFACE)
            else:
                pygame.display.set_mode((1280, 720), DOUBLEBUF|HWSURFACE)