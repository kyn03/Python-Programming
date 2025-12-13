import pygame
import sys
import random

pygame.init()

screen_width = 800
screen_height = 600

blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

explosion_sound = pygame.mixer.Sound("explosion.wav")

lives = 5
kill_count = 0
game_over = False

font = pygame.font.SysFont(None, 24)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
            
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("alien.png")
        self.image = pygame.transform.scale(self.image,(30,30))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-50, -10)
        self.speed_y = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > screen_height:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(-50, -10)
            self.speed_y = random.randint(1, 3)
            
    def explode(self):
        explosion_sound.play()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 20))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -2

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()


def reset_game():
    global lives, kill_count, game_over, all_sprites, aliens, bullets, player

    lives = 5                  
    kill_count = 0             
    game_over = False          

    
    all_sprites.empty()
    aliens.empty()
    bullets.empty()

    
    player = Player()
    all_sprites.add(player)

    
    for _ in range(10):
        alien = Alien()
        all_sprites.add(alien)
        aliens.add(alien)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader")

all_sprites = pygame.sprite.Group()
aliens = pygame.sprite.Group()
bullets = pygame.sprite.Group()

reset_game()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                reset_game()

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
                elif event.key == pygame.K_LEFT:
                    player.speed_x = -5
                elif event.key == pygame.K_RIGHT:
                    player.speed_x = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.speed_x = 0

    if not game_over:
        all_sprites.update()

        
        hits = pygame.sprite.groupcollide(aliens, bullets, True, True)
        for hit in hits:
            alien = Alien()
            alien.explode()
            all_sprites.add(alien)
            aliens.add(alien)
            kill_count += 1     

       
        if pygame.sprite.spritecollide(player, aliens, False):
            lives -= 1            
            if lives <= 0:
                game_over = True 

    screen.fill(black)

    all_sprites.draw(screen)

    ui_text = font.render(f"Kills: {kill_count}   Lives: {lives}", True, white)
    screen.blit(ui_text, (10, 10))

    if game_over:
        over_text = font.render("GAME OVER - Press ENTER", True, red)
        x = (screen_width - over_text.get_width()) // 2
        y = (screen_height - over_text.get_height()) // 2
        screen.blit(over_text, (x, y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()