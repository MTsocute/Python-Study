import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite


class WaterDrop(Sprite):
    """ Generate a Water's class """
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load(
            '/Users/momo/Desktop/Python/Project/Practise/images/water_drop.bmp')

        # Make water drop smaller
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.screen = screen

        self.drop_speed = 0.5

        self.rect = self.image.get_rect()

        # Initial Position(Left-Top)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Using the variable to change water drop's vertical position
        self.y = float(self.rect.y)

    def blit_me(self):
        """ Generate a water drop on screen """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Make water dropping """
        self.y += self.drop_speed
        self.rect.y = self.y

    def check_edges(self):
        """ When the rain hit the bottom, we return True """
        screen_rect = self.screen.get_rect()    # Get the value of the bottom
        # Check whether the rain hit the bottom
        if self.rect.bottom > screen_rect.bottom:
            return True


def get_number_x(screen, water_drop_width):
    """ Return the mount of water that a screen can contain """
    available_x = screen.get_rect().width - 2 * water_drop_width   # Available width excluding the edge
    number_x = int(available_x / (2*water_drop_width))  # The number we need
    return number_x

def create_water(water_drops, screen):
    """ Generate a row of water drop on screen """
    water_drop = WaterDrop(screen)
    water_drop_width = water_drop.rect.width
    number_x = get_number_x(screen, water_drop_width)

    # Generate an objection and add it into the group
    for number in range(number_x):
        water_drop_sprite = WaterDrop(screen)
        water_drop.edge_x = \
            water_drop_width + 2 * water_drop_width * number    # Control the edge of each water drop
        water_drop_sprite.rect.x = water_drop.edge_x
        water_drops.add(water_drop_sprite)  # Add into water drop Group

def re_rain(water_drops):
    """ Make it rain again """
    water_drops.update()    # let rain
    # When water drop hits the bottom reset the height and update it
    for water_drop in water_drops.sprites():
        if water_drop.check_edges():
            water_drop.y = 0    # Back to Top
            water_drop.update()


def UI():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Rain~~")
    bg_color = (255,255,255)

    # Generate a water drop obj

    water_drops = Group()

    # Add water drops into Group
    create_water(water_drops, screen)


    while True:
        screen.fill(bg_color)

        # Let water drop dropping
        re_rain(water_drops)

        # let all water drops drawn on the screen
        water_drops.draw(screen)

        # Quit the Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


if __name__ == '__main__':
    UI()