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

        if event.type == pygame.KEYDOWN:
            print("KEYDOWN:", event.key)

        if event.type == pygame.KEYUP:
            print("KEYUP:", event.key)

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse Click:", event.pos)
    
    pygame.display.flip()