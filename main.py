import pygame
import pygame_gui
from blob import Blob
from commands import process_command

pygame.init()

WINDOW_SIZE = (640, 480)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Autonomous Blob")

manager = pygame_gui.UIManager(WINDOW_SIZE)

blob = Blob(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2)

input_textbox = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((50, 400), (300, 30)), manager=manager)
input_textbox.set_allowed_characters("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")

button_parse = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((360, 400), (100, 30)), text='Parse', manager=manager)

clock = pygame.time.Clock()
running = True

command_delay = 1000
command_timer_event = pygame.USEREVENT + 1
command_queue = []
current_command_index = -1  # Add this line before the while loop

font = pygame.font.Font(None, 24)

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

        if event.type == command_timer_event:
            if command_queue:
                word = command_queue.pop(0).lower()
                process_command(blob, word, command_queue)

                if not command_queue:
                    pygame.time.set_timer(command_timer_event, 0)
                else:
                    pygame.time.set_timer(command_timer_event, command_delay)

        manager.process_events(event)

    manager.update(time_delta)

    screen.fill((255, 255, 255))

     # Draw command queue and marker for the currently running command
    y_offset = 10
    for index, cmd in enumerate(command_queue):
        if index == current_command_index:
            cmd_text = font.render(f"> {cmd}", True, (0, 0, 0))
        else:
            cmd_text = font.render(cmd, True, (0, 0, 0))
        screen.blit(cmd_text, (10, y_offset))
        y_offset += 30
    pygame.draw.circle(screen, blob.color, (int(blob.x), int(blob.y)), blob.size)
    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()# Write your code here :-)
