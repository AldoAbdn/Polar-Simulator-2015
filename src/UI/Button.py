from UI.Text import Text
import pygame

#Button class that inherits from Text. Only difference is bg colour specified 
class Button(Text):
    def __init__(self, x, y, text, colour, background, font="Impact", size=72):
        Text.__init__(self, x, y, text, colour, font, size)
        self.text = text
        self.background = background
        self.updateTextWithBackground(text)

    #Used to change displayed text of an instance and update Rect object with new dimensions
    def updateTextWithBackground(self, text):
        self.text = text
        self.surface = self.font.render(self.text, True, self.colour, self.background)
        self.rect = self.surface.get_rect(center = (self.x, self.y))

    #Checks if Text object has been clicked and returns a value if clicked or if not
    def clicked(self): 
        events = pygame.event.get()
        #Loops thourgh events looking for mouse up, then checks if mouseclick collides with Text object
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                mouseClick = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouseClick):
                    return False
        return True