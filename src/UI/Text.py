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