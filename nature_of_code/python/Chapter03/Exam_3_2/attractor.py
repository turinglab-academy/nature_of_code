import pygame

class Attractor:
    def __init__(self, screen):
        self.screen = screen
        self.position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.mass = 20
        self.G = 1

    def attract(self, mover):
        # 힘의 방향 계산
        force = self.position - mover.position
        # 두 객체의 중심점 간의 거리
        distance = force.magnitude()
        # 두 객체간의 거리가 너무 극단적(너무 가깝거나, 너무 먼)이지 않도록, 값을 조정        
        distance = pygame.math.clamp(distance, 5, 25)

        # 중력의 크기 계산
        strength = (self.G * self.mass * mover.mass) / (distance * distance)        
        # 힘과 방향을 적용한 힘을 구함
        force.scale_to_length(strength)
        return force

    # Method to display
    def show(self):
        color = (175, 175, 175)

        pygame.draw.circle(self.screen, color, self.position, self.mass)
        pygame.draw.circle(self.screen, (0, 0, 0), self.position, self.mass, 1)
