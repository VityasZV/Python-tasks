import pygame
from random import randrange

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

SZ = 100, 80

windows, amount_of_windows = [], 0
lines, amount_of_lines = [], 0
while True:
    pygame.time.set_timer(pygame.USEREVENT, 500)
    pygame.time.wait(250)
    e = pygame.event.wait()

    if e.type is pygame.QUIT:
        print("QUIT")
        break
    elif e.type is pygame.MOUSEBUTTONDOWN:
        if e.button == 3:
            color = pygame.Color(randrange(100, 256), randrange(100, 256), randrange(100, 256))
            windows.append((amount_of_windows, color, pygame.Rect(e.pos, SZ)))
            amount_of_windows += 1
        elif e.button == 1:
            color = pygame.Color(randrange(100, 256), randrange(100, 256), randrange(100, 256))
            start_pos = e.pos
            end_pos = start_pos
            while True:
                e = pygame.event.wait()
                if e.type == pygame.MOUSEMOTION:
                    end_pos = e.pos
                    continue
                break
            lines.append((amount_of_lines, color, start_pos, end_pos))
            amount_of_lines += 1
    else:
        for (i, color, rect) in reversed(windows):
            if hasattr(e, "pos") and rect.collidepoint(e.pos):
                print(f"{e} to {i}")
                break
        else:
            print(e)
    screen.fill(0)
    for i, color, rect in windows:
        screen.fill(color, rect)
    for i, color, start, end in lines:
        pygame.draw.line(screen, color, start, end)
    pygame.display.flip()
    continue
