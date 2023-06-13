import time
from random import randint
import pygame

pygame.init()
'''создаём окно программы'''
back = (200, 255, 255)  # цвет фона (background)
mw = pygame.display.set_mode((500, 500))  # окно программы (main window)
mw.fill(back)
clock = pygame.time.Clock()
'''класс прямоугольник'''


class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)  # прямоугольник
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):  # обводка существующего прямоугольника
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


'''класс надпись'''


class Label(Area):

    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
GREEN = (0, 255, 51)
RED = (255, 0, 0)
cards = []
num_cards = 4
x = 70
for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.set_text('CLICK', 12)
    new_card.outline(DARK_BLUE, 10)
    cards.append(new_card)
    x = x + 100

d = 0
wait = 0
start_time = time.time()
cur_time = start_time
schet = int()
schet_text = Label(320, 0, 50, 50, back)
schet_text.set_text('счёт', 40, DARK_BLUE)
schet_text.draw()
time_text = Label(0, 0, 50, 50, back)
time_text.set_text('Время:', 40, DARK_BLUE)
time_text.draw()
timer = Label(50, 55, 50, 40, back)
timer.set_text('0', 40, DARK_BLUE)
timer.draw()
while True:
    new_time = time.time()
    if new_time - cur_time >= 1:
        timer.set_text(str(int(new_time - start_time)), 40, DARK_BLUE)
        timer.draw(0, 0)
        cur_time = new_time
    if wait == 0:
        wait = 20
        click = randint(1, num_cards)
        for i in range(num_cards):
            if (i + 1) == click:
                cards[i].draw(10, 40)
            else:
                cards[i].fill()
                cards[i].outline(DARK_BLUE, 10)
    else:
        wait -= 1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x, y):
                    if i + 1 == click:
                        cards[i].color(GREEN)
                        d += 1
                    else:
                        cards[i].color(RED)
                        d -= 1
                    if d == 5:
                        break

                    cards[i].fill()

    pygame.display.update()
    clock.tick(40)
