import pygame

class Dropdown:
    def __init__(self, options, x, y):
        self.options = options
        self.selectedIndex = 0
        self.x = x
        self.y = y

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, 100, 20))

        # Render the text for the dropdown
        text = pygame.font.SysFont(None, 20).render(self.options[self.selectedIndex], True, (0, 0, 0))

        # Blit the text to the screen
        surface.blit(text, (self.x + 5, self.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if event.x >= self.x and event.x <= self.x + 100 and event.y >= self.y and event.y <= self.y + 20:
                self.selectedIndex = (self.selectedIndex + 1) % len(self.options)

class Button:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, 100, 20))

        # Render the text for the button
        text = pygame.font.SysFont(None, 20).render(self.text, True, (0, 0, 0))

        # Blit the text to the screen
        surface.blit(text, (self.x + 5, self.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if event.x >= self.x and event.x <= self.x + 100 and event.y >= self.y and event.y <= self.y + 20:
                print("Button clicked!")

import pygame

class UI:
    def __init__(self):
        self.algorithms = ["Algorithm 1", "Algorithm 2", "Algorithm 3"]
        self.sizes = ["Small", "Medium", "Large"]
        self.num_drones = [1, 2, 3, 4, 5]

        self.algorithm_dropdown = Dropdown(self.algorithms, 10, 10)
        self.size_dropdown = Dropdown(self.sizes, 10, 40)
        self.num_drones_dropdown = Dropdown(self.num_drones, 10, 70)
        self.execute_button = Button("Execute", 10, 100)

        self.font = pygame.font.SysFont(None, 20)

    def draw(self, surface):
        self.algorithm_dropdown.draw(surface)
        self.size_dropdown.draw(surface)
        self.num_drones_dropdown.draw(surface)
        self.execute_button.draw(surface)

    def handle_event(self, event):
        self.algorithm_dropdown.handle_event(event)
        self.size_dropdown.handle_event(event)
        self.num_drones_dropdown.handle_event(event)
        self.execute_button.handle_event(event)

def main():
    pygame.init()

    surface = pygame.display.set_mode((200, 200))
    pygame.display.set_caption("UI Example")

    ui = UI()

    running = True
