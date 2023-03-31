import random
import math
import pygame
from blob_manager import BlobManager
from commands import process_command
from pygame.time import delay

class Blob:
    blob_count = 0

    def __init__(self, x, y):
        self.name = f"Blob{Blob.blob_count}"
        self.x = x
        self.y = y
        self.size = 20
        self.color = (255, 0, 0)
        self.speed = 5
        self.direction = random.randint(0, 360)
        self.vision_radius = 100
        self.command_queue = []
        self.last_command_queue = []
        self.command_delay = 500  # Set the initial command delay (in milliseconds)
        Blob.blob_count += 1
        self.command_dictionary = {
            'forward': self.move_forward,
            'back': self.move_back,
            'left': self.turn_left,
            'right': self.turn_right,
            'speed': self.set_speed,
            'color': self.set_color
        }

    def move_forward(self):
        dx = self.speed * math.cos(math.radians(self.direction))
        dy = self.speed * math.sin(math.radians(self.direction))
        self.x += dx
        self.y += dy

    def move_back(self):
        dx = self.speed * math.cos(math.radians(self.direction))
        dy = self.speed * math.sin(math.radians(self.direction))
        self.x -= dx
        self.y -= dy

    def turn_left(self):
        self.direction -= 90

    def turn_right(self):
        self.direction += 90

    def set_speed(self, speed):
        self.speed = float(speed)

    def set_color(self, color):
        if color == 'red':
            self.color = (255, 0, 0)
        elif color == 'green':
            self.color = (0, 255, 0)
        elif color == 'blue':
            self.color = (0, 0, 255)

    def process_command(self, command):
        word, *args = command.split()
        word = word.lower()
        print(f"Processing command: {word}")

        if word in self.command_dictionary:
            if args:
                self.command_dictionary[word](*args)
            else:
                self.command_dictionary[word]()
        else:
            print(f"Unknown command: {word}")

        print(f"Blob '{self.name}': Command '{word}', Args: {args}")  # Debug print statement

    def process_commands(self, command_queue, loop_mode):
        if not command_queue:
            return

        index = 0

        while True:
            command = command_queue[index % len(command_queue)]
            self.process_command(command)

            pygame.time.delay(self.command_delay)  # Add a delay between commands
            index += 1

            if not loop_mode and index >= len(command_queue):
                break
