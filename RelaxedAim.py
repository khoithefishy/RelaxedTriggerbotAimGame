# Clock
import pygame
from pygame import mouse
import random
import ctypes

#initialize screen
pygame.init()
screen_width = 1600
screen_height = 900
screen= pygame.display.set_mode((screen_width,screen_height))
clock= pygame.time.Clock()
running = True
red = (255,0,0)
green = (0,255,0)
mouse_pos = mouse.get_pos()
pygame.mouse.set_visible(False)


class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    def draw(self):
        pygame.draw.circle(screen, (self.color),(self.x, self.y),self.radius)
    #Check if cursor is within circle
    def detect_mouse(self, mouse_pos):
        circle_center = (self.x, self.y)
        distance = pygame.math.Vector2(circle_center).distance_to(mouse_pos)
        return distance <= self.radius
    def difficulty(self, amount):
        self.radius += amount
circle_radius = 30
circle_circumference = circle_radius * 2
random_x = random.randint(circle_radius,screen_width)
random_y = random.randint(circle_radius,screen_height)
random_2x = random.randint(circle_radius,screen_width)
random_2y = random.randint(circle_radius,screen_height)
random_3x = random.randint(circle_radius,screen_width)
random_3y = random.randint(circle_radius,screen_height)
circle = Circle(random_x, random_y, circle_radius, red)
circle2 = Circle(random_2x, random_2y, circle_radius, red)
circle3 = Circle(random_3x, random_3y, circle_radius, red)
circle_cursor = Circle(circle.x, circle.y, 5, green)


while running:
    mouse_pos = mouse.get_pos()
    circle_cursor.x = mouse_pos[0]
    circle_cursor.y = mouse_pos[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =  False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_a:
                circle.difficulty(5)
                circle2.difficulty(5)
                circle3.difficulty(5)
            if event.key == pygame.K_d:
                circle.difficulty(-5)
                circle2.difficulty(-5)
                circle3.difficulty(-5)
        if circle.detect_mouse(mouse_pos):
            random_x = random.randint(circle_circumference, screen_width - circle_circumference)
            random_y = random.randint(circle_circumference, screen_height- circle_circumference)
            circle.x = random_x
            circle.y = random_y
        if circle2.detect_mouse(mouse_pos):
            random2_x = random.randint(circle_circumference, screen_width - circle_circumference)
            random2_y = random.randint(circle_circumference, screen_height- circle_circumference)
            circle2.x = random2_x
            circle2.y = random2_y
        if circle3.detect_mouse(mouse_pos):
            random3_x = random.randint(circle_circumference, screen_width - circle_circumference)
            random3_y = random.randint(circle_circumference, screen_height- circle_circumference)
            circle3.x = random3_x
            circle3.y = random3_y
    screen.fill((0, 0, 0))
    circle.draw()
    circle2.draw()
    circle3.draw()
    circle_cursor.draw()
    pygame.display.update()
    clock.tick(360)