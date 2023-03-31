import pygame
import pygame_gui
from pygame_gui.elements import UITextEntryLine, UIButton, UIDropDownMenu

def create_blob_ui(manager, num_blobs):
    options = [f"Blob{i-1}" for i in range(1, num_blobs+1)]
    blob_select_dropdown = UIDropDownMenu(
        options_list=options,
        starting_option=options[0],
        relative_rect=pygame.Rect((50, 400), (150, 30)),
        manager=manager,
    )
    return blob_select_dropdown
def create_ui(manager):
    input_textbox = UITextEntryLine(
        relative_rect=pygame.Rect((50, 50), (300, 30)),
        manager=manager,
    )

    button_run = UIButton(
        relative_rect=pygame.Rect((160, 100), (100, 30)),
        text="Run",
        manager=manager,
    )

    button_loop = UIButton(
        relative_rect=pygame.Rect((270, 100), (100, 30)),
        text="Loop",
        manager=manager,
    )

    return input_textbox, button_run, button_loop

