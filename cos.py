import pygame

pygame.init()

def main():
    screen = pygame.display.set_mode((512,512))
    
    run = True
    while run:
        box = pygame.draw.rect(screen, (255,0,0), pygame.Rect(30,30,x,y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pass
            pass
        pygame.display.update()
        pass
    pass

if __name__ == '__name__':
    x = input('Podaj x: ')
    y = input('Podaj y: ')
    main()
