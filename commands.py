import math

def process_command(blob, word, command_queue):
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
