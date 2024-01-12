import pygame, math
pygame.init()
win = pygame.display.set_mode((500, 480))
pygame.display.set_caption('The Game...')
clock = pygame.time.Clock()
tree = pygame.image.load('Treeupcale128128.png')
bg = pygame.image.load('grass.png')
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
        self.hitbox = pygame.Rect(self.x, self.y+64, self.width/4, self.height/3)
    def draw(self, win):
         win.blit(tree, (self.x, self.y))
         self.hitbox = pygame.Rect(self.x, self.y+64, self.width/4, self.height/3)
def drawOnScreen():
    screenWidth, screenHeight = win.get_size()
    imageWidth, imageHeight = bg.get_size()
    tilesX = math.ceil(screenWidth / imageWidth)
    tilesY = math.ceil(screenHeight / imageHeight)
    for x in range(tilesX):
        for y in range(tilesY):
            win.blit(bg, (x * imageWidth, y * imageHeight))
    man.draw(win)
    wall.draw(win)
    pygame.display.update()
man = Player(30, 30, 60, 60) 
wall = block(100, 100, 200, 200) 
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if man.y == 0:
            pass
        else:
            if man.hitbox.colliderect(wall.hitbox):
                if man.hitbox.top - wall.hitbox.bottom < 10:
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
            if man.hitbox.colliderect(wall.hitbox):
                if wall.hitbox.top - man.hitbox.bottom < 10:
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
print(man.hitbox.top - wall.hitbox.bottom)
print(wall.hitbox.top - man.hitbox.bottom)