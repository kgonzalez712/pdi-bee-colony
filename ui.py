import pygame
import pygame_gui

def create_text_input(screen, x, y, width, height, text=""):
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height), 1)
    if text:
        text_surface = font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (x + 5, y + 5))

def create_button(screen, x, y, width, height, text):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height), 1)
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (x + 5, y + 5))

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    font = pygame.font.SysFont(None, 24)

    text_input = create_text_input(screen, 100, 100, 200, 50, "Enter program name:")
    button = create_button(screen, 300, 100, 100, 50, "Execute")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    # Execute the program with the params in the text input
                    program = text_input.text
                    params = text_input.text.split(" ")
                    # TODO: Execute the program with the params
                    pass

        screen.fill((0, 0, 0))

        text_input.draw(screen)
        button.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
