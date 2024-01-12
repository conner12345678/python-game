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
    

    def Dialogue():
        pass


class Enemy(Entity):



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



# Here I init some variables and set up some basic stats for our character. Our chacter has colision but NPC's will not. When walking over them a text prompt will appear. Thats how talking to NPC's will work. Enemy's will have colision but i haven't set that up yet. I also know i haven't put anything on screen yet. Thats 100% your job, fuck that. Im finally going to bed at 2am.



class Item():
    pass

player_character = Player()






















# class block:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.hitbox = pygame.Rect(self.x, self.y+64, self.width/4, self.height/3)

#     def draw(self, win):
#          win.blit(tree, (self.x, self.y))
#          self.hitbox = pygame.Rect(self.x, self.y+64, self.width/4, self.height/3)

# def drawOnScreen():
#     screenWidth, screenHeight = win.get_size()
#     imageWidth, imageHeight = bg.get_size()
#     tilesX = math.ceil(screenWidth / imageWidth)
#     tilesY = math.ceil(screenHeight / imageHeight)
#     for x in range(tilesX):
#         for y in range(tilesY):
#             win.blit(bg, (x * imageWidth, y * imageHeight))
#     pygame.display.update()


# while run:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w] or keys[pygame.K_UP]:
#         if man.y == 0:
#             pass
#         else:
#             if man.hitbox.colliderect(wall.hitbox):
#                 if man.hitbox.top - wall.hitbox.bottom < 10:
#                     pass
#             else:
#                 man.y -= man.vel
#     if keys[pygame.K_a] or keys[pygame.K_LEFT]:
#         if man.x == 0:
#             pass
#         else:
#             man.x -= man.vel
#     if keys[pygame.K_s] or keys[pygame.K_DOWN]:
#         if man.y == 480-man.height:
#             pass
#         else:
#             if man.hitbox.colliderect(wall.hitbox):
#                 if wall.hitbox.top - man.hitbox.bottom < 10:
#                     pass
#             else:
#                 man.y += man.vel
#     if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
#         if man.x == 500-man.width:
#             pass
#         else:
#             man.x += man.vel
#     drawOnScreen()

# pygame.quit