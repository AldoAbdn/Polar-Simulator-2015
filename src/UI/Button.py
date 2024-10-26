import Text

#Button class that inherits from Text. Only difference is bg colour specified 
class Button(Text):
    def __init__(self):
        Text.__init__(self)
        self.text = "START"
        self.y = 640
        self.surface = self.font.render(self.text, True, (0,0,0), (255,0,0))
        self.rect = self.surface.get_rect(center = (self.x, self.y))