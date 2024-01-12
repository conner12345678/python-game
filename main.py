import pygame, math, random
pygame.init()
window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('The Game...')
clock = pygame.time.Clock()
tree = pygame.image.load('Treeupcale128128.png')
background = pygame.image.load('grass.png')
game_state = True


'''Changed varaible names because, fuck you'''



def make_colision_lines(cross_points, width, height):
    return [pygame.Rect(cross_points[0][0], cross_points[0][1], width, 1),
            pygame.Rect(cross_points[2][0], cross_points[2][1], 1, height),
            pygame.Rect(cross_points[3][0], cross_points[3][1], width, 1),
            pygame.Rect(cross_points[1][0], cross_points[1][1], 1, height)]


'''                             First       X,Y




X,Y      Second                                                        Third   X,Y




                               fourth      X,Y
    
I make Some points in the above order then when making colision lines i use the values to make ultra thin rectangles seperate from the main hitbox. I store the rectangles in a list which is stored in a variable so that it can be acessed easy. As well, i go clockwise when creating the lines. If it bothers you that the point creation isn't the same, change it nerd.
'''


def Colision_Check(colision_lines):
    pass


class Game_Object():
    def __init__(self, x, y, width, height, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.hitbox = pygame.Rect(x, y, width, height)
        self.cross_points = [[x, y + (height / 2)], [x - (width / 2), y], [x + (width / 2), y], [x, y - (height / 2)]]
        self.colision_lines = make_colision_lines(self.cross_points, width, height)


    # I init the variables i will use later. I use a function to make 4 different rectangles to represent different sides of the player so that when coliding, player input will not be taken in that same manner.


class Entity():
    def __init__(self, x, y, width, height, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.hitbox = pygame.Rect(x, y, width, height)
    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    def Dialogue(self):
        font = pygame.font.SysFont('comicsans', 100)
        text = font.render("test", 1, (0, 0, 255))
        window.blit(text, (self.x, self.y-20))
        pygame.display.update()
        print("this")


class Enemy(Entity):
    pass


class Player():
    def __init__(self, x, y, width, height, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.hitbox = pygame.Rect(x, y, width, height)
        self.cross_points = [[x, y + (height / 2)], [x - (width / 2), y], [x + (width / 2), y], [x, y - (height / 2)]]
        self.colision_lines = make_colision_lines(self.cross_points, width, height)                          
        self.strengh = 10
        self.mana = 10
        self.stamina = 100
        self.luck = 100
        self.RNG = 100
    def draw(self, win):
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.width, self.height))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)


# Here I init some variables and set up some basic stats for our character. Our chacter has colision but NPC's will not. When walking over them a text prompt will appear. Thats how talking to NPC's will work. Enemy's will have colision but i haven't set that up yet. I also know i haven't put anything on screen yet. Thats 100% your job, fuck that. Im finally going to bed at 2am.

def drawOnScreen():
    screenWidth, screenHeight = window.get_size()
    imageWidth, imageHeight = background.get_size()
    tilesX = math.ceil(screenWidth / imageWidth)
    tilesY = math.ceil(screenHeight / imageHeight)
    for x in range(tilesX):
        for y in range(tilesY):
            window.blit(background, (x * imageWidth, y * imageHeight))
    player_character.draw(window)
    npc.draw(window)
    pygame.display.update()

class Item():
    pass
player_character = Player(30, 30, 60, 60, 180)
npc = Entity(100, 100, 60, 60, 180)
while game_state:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = False
    if npc.hitbox.colliderect(player_character.hitbox):
            npc.Dialogue()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if player_character.y == 0:
            pass
        else:
            player_character.y -= 5
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if player_character.y == 600-player_character.height:
            pass
        else:
            player_character.y += 5
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if player_character.x == 0:
            pass
        else:
            player_character.x -= 5
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if player_character.x == 1200-player_character.width:
            pass
        else:
            player_character.x += 5
    drawOnScreen()
pygame.quit