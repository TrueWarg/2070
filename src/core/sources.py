import pygame
import os

def load_image(path):
    full_path = os.path.join("assets", "images", path)
    print(full_path)
    return pygame.image.load(full_path).convert_alpha()

def load_sound(path):
    full_path = os.path.join("assets", "sounds", "sfx", path)
    return pygame.mixer.Sound(full_path)

def load_theme(path):
    full_path = os.path.join("assets", "sounds", "theme", path)
    return full_path