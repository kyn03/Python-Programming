import pygame, sys, random
from pygame.locals import *

# 게임 재시작 함수
def GameRestart(_score):
    restart_screen = pygame.display.set_mode((800, 500))
    pygame.font.init()
    restart_font = pygame.font.SysFont('Sans', 60, True, True)
    restart_message = 'Press the space key to restart'
    restart_message_object = restart_font.render(restart_message, True, (0, 0, 0))
    score_message = 'Your score is ' + str(_score)
    score_message_object = restart_font.render(score_message, True, (0, 0, 255))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.init()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_SPACE:
                return main()
            
        restart_screen.fill((255, 255, 255))
        restart_screen.blit(restart_message_object, (25, 0))
        restart_screen.blit(score_message_object, (25, 100))
        pygame.display.update()

# 메인 게임 함수
def main():
    # 게임 초기화 정보
    pygame.init()
    screen_width = 800
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Jump Game')

    # 배경 이미지
    bgImage = pygame.image.load('backgroundImg.jpg')
    bgImage = pygame.transform.scale(bgImage, (screen_width, screen_height))

    # 주인공 객체 생성
    player = pygame.Rect((screen_width-50)/2, screen_height-50, 50, 50)
    player_img = pygame.image.load('fox.png')
    player_img = pygame.transform.scale(player_img, (50, 50))

    # 포도 객체 생성
    grapes = []
    for i in range(20):
        grape = pygame.Rect(random.randint(0, screen_width-40), random.randint(350, 400), 40, 40)
        grapes.append(grape)
    grape_img = pygame.image.load('grape.png')
    grape_img = pygame.transform.scale(grape_img, (40, 40))

    # 몬스터 객체 생성
    monster = pygame.Rect(0, 440, 60, 60)
    monster_img = pygame.image.load('monster.png')
    monster_img = pygame.transform.scale(monster_img, (60, 60))

    # 게임 속도 조절
    clock = pygame.time.Clock()
    game_speed = 0.5
    monster_speed = 0.3

    # 중력 엔진
    y_vel = 0

    # 폰트 객체 생성
    font = pygame.font.SysFont('Sans', 30, True, True)

    # 점수 변수
    score = 0

    while True:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keyInput = pygame.key.get_pressed()
        if keyInput[K_LEFT] and player.left >= 0:
            player.left -= game_speed * dt
        if keyInput[K_RIGHT] and player.right <= screen_width:
            player.right += game_speed *dt

        # 중력 엔진 만들기
        player.top += y_vel
        y_vel += 1

        # 포도와 플레이어의 충돌
        for grape in grapes:
            if player.colliderect(grape):
                grapes.remove(grape)
                score += 1

        # 포도를 다 먹으면 다시 포도 20개 생성
        if len(grapes) == 0:
            for i in range(20):
                grape = pygame.Rect(random.randint(0, screen_width-40), random.randint(350, 400), 40, 40)
                grapes.append(grape)

        # 몬스터 좌/우 움직이기, 플레이어와 충돌
        monster.right += monster_speed * dt
        if monster.right >= screen_width:
            monster.right = screen_width
            monster_speed *= -1
        
        elif monster.left <= 0:
            monster.left = 0
            monster_speed *= -1

        elif monster.colliderect(player):
            GameRestart(score)

        if player.bottom >= 500:
            y_vel = 0
            if keyInput[K_SPACE]:
                y_vel = -18

        # 점수 메시지 만들기
        score_message = font.render('SCORE: ' + str(score), True, (0, 0, 255))
        

        screen.blit(bgImage, (0, 0))
        screen.blit(player_img, player)
        screen.blit(score_message, (0, 0))
        screen.blit(monster_img, monster)
        
        # 포도 그리기
        for grape in grapes:
            screen.blit(grape_img, grape)


        pygame.display.update()

main()