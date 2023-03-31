import pygame
import pygame_gui
import random
import math
from blob import Blob
from blob_manager import BlobManager
from ui import create_ui, create_blob_ui
from commands import process_command

pygame.init()

WINDOW_SIZE = (640, 480)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Autonomous Blob")

manager = pygame_gui.UIManager(WINDOW_SIZE)
blob_manager = BlobManager()
for _ in range(3):  # Change the number of blobs you want to create
    random_x = random.randint(0, WINDOW_SIZE[0])
    random_y = random.randint(0, WINDOW_SIZE[1])
    blob = Blob(random_x, random_y)
    blob_manager.add_blob(blob)

input_textbox, button_run, button_loop = create_ui(manager)
blob_select_dropdown = create_blob_ui(manager, len(blob_manager.blobs))

clock = pygame.time.Clock()
running = True

# Command delay variable and timer event
command_delay = 1000  # in milliseconds
command_timer_event = pygame.USEREVENT + 1
command_queue = []
loop_mode = False

while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT and hasattr(event, 'ui_object_id'):
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_run:
                    command = input_textbox.get_text()
                    selected_blob_name = blob_select_dropdown.selected_option
                    selected_blob = next((blob for blob in blob_manager.blobs if blob.name == selected_blob_name), None)
                    selected_blob.command_queue = command.split()
                    if not loop_mode:
                        pygame.time.set_timer(command_timer_event, command_delay)
                    else:
                        pygame.time.set_timer(command_timer_event, 0)

                elif event.ui_element == button_loop:
                    loop_mode = not loop_mode
                    button_loop.set_text("Loop" if not loop_mode else "Unloop")

        if event.type == pygame.USEREVENT + 1 and not loop_mode:
            for blob in blob_manager.blobs:
                blob.process_commands(blob.command_queue, loop_mode)

            if loop_mode:
                pygame.time.set_timer(command_timer_event, command_delay)
            else:
                pygame.time.set_timer(command_timer_event, 0)

        manager.process_events(event)

    manager.update(time_delta)
    screen.fill((255, 255, 255))
    for blob in blob_manager.blobs:
        pygame.draw.circle(screen, blob.color, (int(blob.x), int(blob.y)), blob.size)
    manager.draw_ui(screen)

    pygame.display.update()

pygame.quit()
