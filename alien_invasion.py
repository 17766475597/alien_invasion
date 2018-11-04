import pygame;

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStates
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化游戏并创建一个游戏对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建Play按钮
    play_button = Button(ai_settings,screen,"Play")

    #创建一个用于存储游戏统计信息的实例
    stats = GameStates(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创造一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    bg_color=(230,230,230)

    #alien = Alien(ai_settings,screen)

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        if stats.ship_left>0:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_alien(ai_settings,screen,stats,sb,ship,aliens,bullets)
            #print(len(bullets))

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

        #让最近绘制的屏幕可见
        pygame.display.flip()


run_game()