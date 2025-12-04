import pygame

print("pygame 초기화 전")

pygame.init()  # pygame 기능 사용 준비
print("pygame 초기화 완료")

pygame.quit  # pygame 종료
print("pygame 종료 완료")

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()