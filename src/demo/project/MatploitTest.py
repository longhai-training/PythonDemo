import sys
import pygame
class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def run_game():
# 初始化游戏并创建一个屏幕对象 ❶
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
# 开始游戏的主循环 ❸
    while True:
# 监视键盘和鼠标事件 ❹
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() # 让最近绘制的屏幕可见 ❻
        pygame.display.flip()
run_game()