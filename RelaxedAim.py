# Clock
import pygame
from pygame import mouse
import random
import ctypes
import time
# initialize screen
pygame.init()
pygame.font.init()
pygame.display.set_caption("Relaxed Aim")
screen_width = 1600
screen_height = 900
screen_center = (screen_width / 2, screen_height / 2)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
blue = (0, 0, 139)

mouse_pos = mouse.get_pos()
pygame.mouse.set_visible(False)
hit_sfx = pygame.mixer.Sound('hitsfx.WAV')
score = 0
hard = 20
easy = 70

# Display font
font = pygame.font.Font(None, 30)


# Create Circle Class
class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    # Function --> Draws, detect the mouse, size, sfx
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    # Check if cursor is within circle
    def detect_mouse(self, mouse_pos):
        circle_center = (self.x, self.y)
        distance = pygame.math.Vector2(circle_center).distance_to(mouse_pos)
        return distance <= self.radius

    def difficulty(self, amount):
        self.radius += amount
        if self.radius <= 5:
            self.radius = 5

    def sfx(self):
        pygame.mixer.Sound.play(hit_sfx)


circle_radius = 30
circle_circumference = circle_radius * 2
random_x = random.randint(circle_radius, screen_width)
random_y = random.randint(circle_radius, screen_height)
circle = Circle(random_x, random_y, circle_radius, red)
circle_cursor = Circle(circle.x, circle.y, 10, green)
circles = []


for i in range(3):
    random_x = random.randint(circle_radius, screen_width)
    random_y = random.randint(circle_radius, screen_height)
    circles.append(Circle(random_x, random_y, circle_radius, red))

current_state= True
state = "ACTIVE"

while running:
    mouse_pos = mouse.get_pos()
    circle_cursor.x = mouse_pos[0]
    circle_cursor.y = mouse_pos[1]
    random_x = random.randint(circle_circumference, screen_width - circle_circumference)
    random_y = random.randint(circle_circumference, screen_height - circle_circumference)
    for event in pygame.event.get():
        text = font.render(f'Score: {score}', True, white)
        text_circle_size = font.render(f'Size: {circle.radius}', True, white)
        text_difficulty = font.render('Press 1,2 to increase/decrease circles.', True, white)

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                for circle in circles:
                    circle.difficulty(5)
            if event.key == pygame.K_d:
                for circle in circles:
                    circle.difficulty(-5)
            if event.key == pygame.K_1:
                circles.append(Circle(random_x, random_y, circle.radius, red))
            if event.key == pygame.K_2:
                circles.remove(circle)
            elif event.key == pygame.K_ESCAPE:
                    current_state = not current_state
                    if not current_state:
                        state = "PAUSED"
                    else:
                        state = "ACTIVE"



        screen.fill((0, 0, 0))

        if state == "ACTIVE":
            for circle in circles:
                circle.draw()
                if circle.detect_mouse(mouse_pos):
                    circle.x = random_x
                    circle.y = random_y
                    circle.sfx()
                    if circle.radius <= hard:
                        score += 200
                    elif circle.radius >= easy:
                        score += 50
                    else:
                        score += 100

            screen.blit(text, (50, 30))
            screen.blit(text_circle_size, (50, 60))
            screen.blit(text_difficulty, (50, 90))

        if state == "PAUSED":
            screen.fill(blue)
            text_paused = font.render('PAUSED', True, white)
            screen.blit(text_paused, screen_center)


        circle_cursor.draw()
        pygame.display.update()
        clock.tick(360)