# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from random import random

import pygame


class Mover:
    def __init__(self, screen: pygame.Surface, x, y, mass):
        self.screen = screen
        self.mass = mass
        self.radius = mass * 8
        self.position = pygame.Vector2(x, y)
        self.angle = 0
        self.angleVelocity = 0
        self.angleAcceleration = 0
        # x, y 축 속력을 [-1, 1]로 생성
        self.velocity = pygame.Vector2(random() * 2 - 1, random() * 2 - 1)
        self.acceleration = pygame.Vector2()

    def applyForce(self, force):
        # 외부의 힘을 객체에 적용
        pass

    def update(self):
        pass

    def show(self):
        pass
