from asyncio import sleep
from collections import deque
from logging import RootLogger
from random import randint
import pygame
screen = None
pygame.init()
width =420 #210
height=440 #220
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
done=False
pygame.display.set_caption("neopix")
toggle_eraser=False
toggl_simetry=False

bg = ((255,255, 255))
BLACK = ((0,0,0))

def r_red():
    r = randint(0, 255)
    return r
def r_green():
    g = randint(0, 255)
    return g
def r_blue():
    b = randint(0, 255)
    return b

def grid():
    for i in range(0, 20):
        for j in range(0, 20):
            square = pygame.Rect(i*20,j*20,20,20)
            pygame.draw.rect(screen, BLACK, square,1)
    for i in range (0, 20):
        for j in range(20, 21):
             square = pygame.Rect(i*20,j*20,20,20)
             pygame.draw.rect(screen, BLACK, square)
    for i in range (0, 20):
        for j in range(21, 22):
             square = pygame.Rect(i*20,j*20,20,20)
             pygame.draw.rect(screen, ((r_red(), r_green(),r_blue())), square)

def clear():
    for i in range(0, 20):
            for j in range(0, 20):
                square = pygame.Rect(i*20,j*20,20,20)
                pygame.draw.rect(screen, ((225, 225, 225)), square)
    for i in range (0, 20):
            for j in range(20, 21):
                 square = pygame.Rect(i*20,j*20,20,20)
                 pygame.draw.rect(screen, BLACK, square)
    for i in range(0, 20):
            for j in range(0, 20):
                square = pygame.Rect(i*20,j*20,20,20)
                pygame.draw.rect(screen, BLACK, square,1)
    for i in range (0, 20):
            for j in range(20, 21):
                 square = pygame.Rect(i*20,j*20,20,20)
                 pygame.draw.rect(screen, BLACK, square)
screen.fill(bg)
grid()
CUTE_PINK =(255,112,223)

sqr_color=(255,112,223)

def simetry_mode():
    mousex,mousey =  pygame.mouse.get_pos()
    lower_bound_x = mousex-(mousex%20)
    higher_bound_x = mousex-(mousex%20)+20 #NU E NECESAR, INCEPE DE LA LB
    lower_bound_y = mousey-(mousey%20)
    higher_bound_y = mousey-(mousey%20)+20 #NU E NECESAR, INCEPE DE LA LB
    box = pygame.Rect(lower_bound_x,lower_bound_y,20,20)
    pygame.draw.rect(screen,(sqr_color),box)
    box = pygame.Rect(abs(380-lower_bound_x),lower_bound_y,20,20)
    pygame.draw.rect(screen,(sqr_color),box)
def draw_square():
    mousex,mousey =  pygame.mouse.get_pos()
    lower_bound_x = mousex-(mousex%20)
    higher_bound_x = mousex-(mousex%20)+20 #NU E NECESAR, INCEPE DE LA LB
    lower_bound_y = mousey-(mousey%20)
    higher_bound_y = mousey-(mousey%20)+20 #NU E NECESAR, INCEPE DE LA LB
    box = pygame.Rect(lower_bound_x,lower_bound_y,20,20)
    pygame.draw.rect(screen,(sqr_color),box)

def eraser():
    mousex,mousey =  pygame.mouse.get_pos()
    lower_bound_x = mousex-(mousex%20)
    higher_bound_x = mousex-(mousex%20)+20 #NU E NECESAR, INCEPE DE LA LB
    lower_bound_y = mousey-(mousey%20)
    higher_bound_y = mousey-(mousey%20)+20 #NU E NECESAR, INCEPE DE LA LB
    box = pygame.Rect(lower_bound_x,lower_bound_y,20,20)
    pygame.draw.rect(screen,((255, 255, 255)),box,0)
    pygame.draw.rect(screen,BLACK,box,1)





while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousextest, mouseytest = pygame.mouse.get_pos()
            if mouseytest <= 400 and mousextest < 400:
                if toggle_eraser == False:
                    if toggl_simetry == False:
                        draw_square()
                    else:
                        simetry_mode()
                else:
                    eraser()
            else:
                sqr_color = screen.get_at(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RSHIFT:
                if toggl_simetry==False:
                    toggl_simetry=True
                else:
                    toggl_simetry=False
            if event.key == pygame.K_LCTRL: 
                clear()
            if event.key == pygame.K_LSHIFT:
                if toggle_eraser == True:
                    toggle_eraser=False
                    pygame.display.set_caption('Draw Mode')
                else:
                    toggle_eraser=True
                    pygame.display.set_caption('Erase Mode')
                    pygame.image.save(screen,"screenshot.jpg")
        
            



    pygame.display.flip()
    clock.tick(20)

    
    


