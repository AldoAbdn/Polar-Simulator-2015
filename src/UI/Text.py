import pygame

#Class to create text objects to display text with no bg colour
class Text:
    def __init__(self, x, y, text, colour, font="Impact", size=72):
        #Assigns parameters as instance variables
        self.font = pygame.font.SysFont(font, size)
        self.text = text
        self.x = x
        self.y = y, 
        self.colour = colour
        #self.colour = (255,0,0)
        #self.x = 640
        #self.y = 500
        #Creates and positions text surface and Rect object
        self.updateText(self.text)

    #Draws a Text object to the screen
    def draw(self, screen):
        screen.blit(self.surface, self.rect)

    #Used to change displayed text of an instance and update Rect object with new dimensions
    def updateText(self, text):
        self.text = text
        self.surface = self.font.render(self.text, True, self.colour)
        self.rect = self.surface.get_rect(center = (self.x, self.y))

