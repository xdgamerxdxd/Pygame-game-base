import pygame

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.entities()
    
    def entities(self):
        pass
    
    def run(self):
        self.main_menu()


def main():

    pygame.init()

    screen = pygame.display.set_mode((700, 700))
    game = Game(screen)
    clock = pygame.time.Clock()

    while game.running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
        
        game.run()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
main()