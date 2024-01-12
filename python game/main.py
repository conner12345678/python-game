import pygame
pygame.init()
win = pygame.display.set_mode((500, 480))
pygame.display.set_caption('The Game...')
clock = pygame.time.Clock()
bg = pygame.image.load('New Piskel-20240109-191930.png')
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
        it = 10
        if wall.hitbox.top - man.hitbox.bottom < it:
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                pass
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if man.x == 500-man.width:
                    pass
                else:
                    man.x += man.vel
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                if man.y == 0:
                    pass
                else:
                    man.y -= man.vel
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if man.x == 0:
                    pass
                else:
                    man.x -= man.vel
        if wall.hitbox.bottom - man.hitbox.top < it:
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                if man.y == 480-man.width:
                    pass
                else:
                    man.y -= man.vel
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if man.x == 500-man.width:
                    pass
                else:
                    man.x += man.vel
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                pass
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if man.x == 0:
                    pass
                else:
                    man.x -= man.vel
    else:
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if man.y == 0:
                pass
            else:
                man.y -= man.vel
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if man.x == 0:
                pass
            else:
                man.x -= man.vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if man.y == 480-man.height:
                pass
            else:
                man.y += man.vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if man.x == 500-man.width:
                pass
            else:
                man.x += man.vel
    drawOnScreen()
pygame.quit