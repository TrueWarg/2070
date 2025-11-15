from typing import List

import pygame

from src.core.resolution import ResolutionHandler
from src.core.sources import load_image, load_theme
from src.scenes.scene import Scene, Handled, NextScene, TerminateApp


class ClassRoom(Scene):
    def __init__(self, resolution_handler: ResolutionHandler):
        super().__init__()
        self.resolution_handler = resolution_handler
        self.background = load_image("background/class_room.png")
        self.background = pygame.transform.scale(self.background, self.resolution_handler.get_scaled_resolution())
        self.theme = load_theme("fucking_school.mp3")
        pygame.mixer.music.load(self.theme)
        pygame.mixer.music.play(-1)

    def handle_events(self, events: List[pygame.event.Event]) -> Handled | NextScene | TerminateApp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return TerminateApp()
            if event.type == pygame.VIDEORESIZE:
                self.resolution_handler.update_resolution((event.w, event.h))
                self.background = pygame.transform.scale(self.background, self.resolution_handler.get_scaled_resolution())
        return Handled()

    def draw(self, screen: pygame.Surface):
        screen.blit(self.background, (0, 0))