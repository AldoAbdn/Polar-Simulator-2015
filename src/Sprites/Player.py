import pygame

#Player class used to create playable character on screen
class Player: 
    def __init__(self, x, y):
        #Scales sprite and crates right and left facing images, sets direction and updates Rec 
        self.rightImage = pygame.transform.smoothscale(pygame.image.load("../assets/player.png"), (100, 200)).convert_alpha()
        self.leftImage = pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("../assets/player.png"), (100, 200)), True, False).convert_alpha()
        self.image = self.leftImage
        self.facingLeft = True
        self.speed = 5
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def setRect(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center = (self.x, self.y))

    #Draws player to the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    #Used to detect WASD presses, and them move character on screen
    def move(self, keys):
        if keys[pygame.K_a]:
            self.facingLeft = True
            self.image = self.leftImage
            #If sprite isnt at edge of screen, decreses x to move sprite
            if self.x > 0:
                self.x = self.x - self.speed
                #Updates Rect with new position
                self.rect.center = (self.x, self.y)
        if keys[pygame.K_d]:
            #Changes direction and sprite to right
            self.facingLeft = False
            self.image = self.rightImage
            #If sprite isnt at right edge of screen moves sprite
            if self.x < 1280:
                self.x = self.x + self.speed
                #Updates Rect to new position
                self.rect.center = (self.x, self.y)
        if keys[pygame.K_w]:
            #Checks if y inst less than 100 or else prite would be drawn in water
            if self.y > 100:
                self.y = self.y - self.speed
                #Updates Rect with new y position
                self.rect.center = (self.x, self.y)
        if keys[pygame.K_s]:
            #Checks to see if y is less than 520 or sprite would end up in 'water'
            if self.y < 520:
                self.y = self.y + self.speed 
                #Updates Rect with new y position
                self.rect.center = (self.x, self.y)