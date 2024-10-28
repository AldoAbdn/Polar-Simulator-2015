from Screens.Screen import Screen
from Sprites.Player import Player
from Sprites.Enemy import Enemy
from Sprites.Projectile import Projectile
import pygame

class Fight(Screen):
    def __init__(self, game) -> None:
        self.player = Player()
        super().__init__("../assets/background.jpg", [self.player], [], game)

    def draw(self):
        super().draw()
        Enemy.draw(self.game.surface)
        Projectile.draw(self.game.surface)

    def handleSprites(self):
        self.running = Enemy.collide(self.player.rect)
        self.game.score += Projectile.collide()
        Enemy.generate()
        Projectile.generate(self.player)
        Enemy.time += self.game.time
        Projectile.time += self.game.time