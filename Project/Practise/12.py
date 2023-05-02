import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group

class Bullet(Sprite):
    def __init__(self, screen, hero):
        super().__init__()
        self.screen = screen

        # Position
        self.rect = pygame.Rect(0,0,25,10)   # Generate a bullet(HxW : 25x10) in original point

        # Shoot bullet from Hero' middle left side
        self.rect.centery = hero.rect.centery
        self.rect.left = hero.rect.left

        # For bullet movement
        self.x = float(self.rect.x)

        # bullets' speed
        self.speed = 1.25
        # bullet's color
        self.color = 60, 60, 60

    def update(self):
        """ move bullets """
        self.x -= self.speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Hero:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load(
            '/Users/momo/Desktop/Python/Project/Practise/images/link.bmp')

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Initial Position
        self.rect.center = self.screen_rect.center

        # For move
        self.centerx = float(self.screen_rect.centerx)
        self.centery = float(self.screen_rect.centery)

        # Hero Speed
        self.speed = 1.5

        # Symbol for direction Movement
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ move hero """
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.centery += self.speed

        elif self.moving_up and self.rect.top > 0:
            self.centery -= self.speed

        elif self.moving_left and self.rect.left > 0:
            self.centerx -= self.speed

        elif self.moving_right and self.rect.right < self.screen_rect.width:
            self.centerx += self.speed

        # Update Position
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


def UI():
    pygame.init()
    screen = pygame.display.set_mode((float(1200), float(800)))  # 1200 width 800 height
    pygame.display.set_caption("Practise")

    bg_color = (0, 0, 255)

    my_hero = Hero(screen)  # Hero Objection
    bullets = Group()   # To store bullet objects

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    my_hero.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    my_hero.moving_right = True
                elif event.key == pygame.K_UP:
                    my_hero.moving_up = True
                elif event.key == pygame.K_DOWN:
                    my_hero.moving_down = True
                # Fire
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, my_hero)
                    bullets.add(new_bullet)


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    my_hero.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    my_hero.moving_right = False
                elif event.key == pygame.K_UP:
                    my_hero.moving_up = False
                elif event.key == pygame.K_DOWN:
                    my_hero.moving_down = False


        screen.fill(bg_color)
        my_hero.update()  # Update the Position
        my_hero.blitme()  # Draw Hero
        bullets.update()  # Update Each bullets' position

        for bullet in bullets:
            bullet.draw_bullet()
            # Delete the bullets who go over the Window
            if bullet.rect.x <= 0:
                bullets.remove(bullet)


        # print(f'The number of leaving bullets: {len(bullets)}')

        pygame.display.flip()


if __name__ == '__main__':
    UI()
