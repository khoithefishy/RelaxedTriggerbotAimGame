# Clock
import pygame
from pygame import mouse
import random
import ctypes

pygame.init()
screen_width = 1600
screen_height = 900
screen= pygame.display.set_mode((screen_width,screen_height))
clock= pygame.time.Clock()
running = True

mouse_pos = mouse.get_pos()

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    def draw(self):
        pygame.draw.circle(screen, (255,0,0),(self.x, self.y),self.radius)
    def detect_mouse(self, mouse_pos):
        circle_center = (self.x, self.y)
        distance = pygame.math.Vector2(circle_center).distance_to(mouse_pos)
        return distance <= self.radius
circle_radius = 100
random_x = random.randint(1,screen_width)
random_y = random.randint(1,screen_height)
random_2x = random.randint(1,screen_width)
random_2y = random.randint(1,screen_height)
random_3x = random.randint(1,screen_width)
random_3y = random.randint(1,screen_height)
circle = Circle(random_x, random_y, circle_radius)
circle2 = Circle(random_2x, random_2y, circle_radius)
circle3 = Circle(random_3x, random_3y, circle_radius)


while running:
    mouse_pos = mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =  False
        if circle.detect_mouse(mouse_pos):
            random_x = random.randint(1, screen_width)
            random_y = random.randint(1, screen_height)
            circle.x = random_x
            circle.y = random_y
        if circle2.detect_mouse(mouse_pos):
            random2_x = random.randint(1, screen_width)
            random2_y = random.randint(1, screen_height)
            circle2.x = random2_x
            circle2.y = random2_y
        if circle3.detect_mouse(mouse_pos):
            random3_x = random.randint(1, screen_width)
            random3_y = random.randint(1, screen_height)
            circle3.x = random3_x
            circle3.y = random3_y
    screen.fill((0, 0, 0))
    circle.draw()
    circle2.draw()
    circle3.draw()
    pygame.display.update()
    clock.tick(360)