import pygame
import pygame_gui
import random
import math

pygame.init()

WINDOW_SIZE = (640, 480)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Autonomous Blob")

manager = pygame_gui.UIManager(WINDOW_SIZE)

class Blob:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.color = (255, 0, 0)
        self.speed = 10
        self.direction = random.randint(0, 360)
        self.vision_radius = 100

blob = Blob(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2)

input_textbox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((50, 400), (300, 30)), manager=manager)
input_textbox.set_allowed_characters("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")

button_parse = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((360, 400), (100, 30)), text='Parse', manager=manager)

clock = pygame.time.Clock()
running = True

# Command delay variable and timer event
command_delay = 1000  # in milliseconds
command_timer_event = pygame.USEREVENT + 1
command_queue = []

while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_parse:
                    command = input_textbox.get_text()
                    input_textbox.set_text("")
                    command_queue = command.split(' ')
                    if not pygame.time.get_ticks():
                        pygame.time.set_timer(command_timer_event, command_delay)

        # Process the command queue with delay between commands
        if event.type == command_timer_event:
            if command_queue:
                word = command_queue.pop(0).lower()

                # Process commands here
                if word == 'forward':
                    dx = blob.speed * math.cos(math.radians(blob.direction))
                    dy = blob.speed * math.sin(math.radians(blob.direction))
                    blob.x += dx
                    blob.y += dy
                elif word == 'back':
                    dx = blob.speed * math.cos(math.radians(blob.direction))
                    dy = blob.speed * math.sin(math.radians(blob.direction))
                    blob.x -= dx
                    blob.y -= dy
                elif word == 'left':
                    blob.direction -= 90
                elif word == 'right':
                    blob.direction += 90
                elif word == 'speed':
                    if command_queue:
                        speed = int(command_queue.pop(0))
                        blob.speed = speed
                elif word == 'color':
                    if command_queue:
                        color = command_queue.pop(0)
                        if color == 'red':
                            blob.color = (255, 0, 0)
                        elif color == 'green':
                            blob.color = (0, 255, 0)
                        elif color == 'blue':
                            blob.color = (0, 0, 255)
                        elif color == 'black':
                            blob.color = (0, 0, 0)
                        elif color == 'gray':
                            blob.color = (100, 100, 100)

                if not command_queue:
                    pygame.time.set_timer(command_timer_event, 0)
                else:
                    pygame.time.set_timer(command_timer_event, command_delay)

        manager.process_events(event)

    manager.update(time_delta)

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, blob.color, (int(blob.x), int(blob.y)), blob.size)
    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()# Write your code here :-)
