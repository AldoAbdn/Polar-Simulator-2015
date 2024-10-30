from Screens.Screen import Screen
from Sprites.Player import Player
from Sprites.Enemy import Enemy
from Sprites.Projectile import Projectile
import pygame

class Fight(Screen):
    def __init__(self, game) -> None:
        self.player = Player(640, 400)
        super().__init__("../assets/background.jpg", [self.player], [], game)

    def draw(self):
        super().draw()
        Enemy.draw(self.game.surface)
        Projectile.draw(self.game.surface)

    def handleSprites(self):
        self.running = Enemy.collide(self.player.rect)
        self.game.score += Projectile.collide()
        self.player.move(self.game.keys)
        Enemy.generate()
        Projectile.generate(self.game.keys, self.player)
        Enemy.move()
        Projectile.move()
        Enemy.time += self.game.time
        Projectile.time += self.game.time

    def reset(self):
        Enemy.reset()
        self.player.setRect(640, 400)
        return super().reset()
        