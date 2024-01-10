import pygame
pygame.init()
win = pygame.display.set_mode((500, 480))
pygame.display.set_caption('The Game...')
clock = pygame.time.Clock()
run = True
class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    def draw(self, win):
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.width, self.height))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
class block:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    def draw(self, win):
         pygame.draw.rect(win, (255, 0, 0), (self.hitbox))
         self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
def drawOnScreen():
    man.draw(win)
    wall.draw(win)
    pygame.display.update()
    win.fill((0, 0, 0))
man = Player(30, 30, 60, 60) 
wall = block(100, 100, 60, 60) 
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if man.hitbox.colliderect(wall.hitbox):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            man.y = man.y + 9
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            man.x = man.x + 9
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            man.y = man.y  - 9
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            man.x = man.x - 9
    else:
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            man.y -= man.vel
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            man.x -= man.vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            man.y += man.vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            man.x += man.vel
    drawOnScreen()
pygame.quit
