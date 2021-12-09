import pygame,cv2, random, os


class Game():
    def __init__(self):
        self.level = 1
        self.level_complete = False
    def update(self, event_list):
        self.draw()
    def draw(self):
        pygame.init()
        WINDOW_WIDTH = 1280
        WINDOW_HEIGHT = 860
        screen = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)
        screen.fill('RED')
        pygame.display.set_caption('Memory Game')
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        BLACK = (0, 0, 0)
        Fps = 60
        clock = pygame.time.Clock()
        game = Game()
        running = True
        while running:
            game_list = pygame.event.get()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            game.update(pygame.event.get())
            pygame.display.update()
            clock.tick(Fps)
        #pygame.quit()
