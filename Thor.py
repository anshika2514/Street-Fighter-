import pygame, random
from Constants import *
from Sprite import *
pygame.init()

class Thor(pygame.sprite.Sprite):
    idleFrames = []
    walkingFrames = []
    punchFrames = []
    kickFrames = []

    def __init__(self):
        super(Thor, self).__init__()
        self.sprite = pygame.image.load("thor.png").convert_alpha()
        self.spritesheet = SpriteSheet(self.sprite)
        self.w = 250
        self.h = 300

        self.loadIdle()
        self.loadWalking()
        self.loadPunch()

        self.image = pygame.Surface((self.w, self.h))
        self.rect = self.image.get_rect()
        self.ground = HEIGHT
        self.rect.x = WIDTH - 450
        self.rect.y = self.ground - self.h - 60
        self.moveX = False
        self.SPEED = 40
        self.move = 0
        self.index = 0

    def update(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.moveX = True
            self.move = self.SPEED
            self.showWalking()
        elif keypressed[pygame.K_LEFT]:
            self.moveX = True
            self.SPEED = 40
            self.move = -self.SPEED
            self.showWalking()
        elif keypressed[pygame.K_RSHIFT]:
            self.showPunch()
        else:
            self.move = 0
            self.showIdle()

        if self.moveX:
            self.rect.x += self.move

    def loadIdle(self):
        self.image = self.spritesheet.getImage(3398, 56, 142, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(3253, 56, 146, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(3104, 56, 150, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(2943, 56, 161, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(2770, 56, 172, 143)
        self.idleFrames.append(self.image)
        self.image = self.spritesheet.getImage(2604, 56, 168, 143)
        self.idleFrames.append(self.image)

    def loadWalking(self):
        self.image = self.spritesheet.getImage(140, 37, 92, 86)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(299, 37, 53, 86)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(421, 37, 55, 86)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(535, 37, 89, 86)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(811, 37, 52, 86)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(935, 37, 55, 84)
        self.walkingFrames.append(self.image)
        self.image = self.spritesheet.getImage(1043, 37, 87, 84)
        self.walkingFrames.append(self.image)

    def loadPunch(self):
        self.image = self.spritesheet.getImage(20, 528, 73, 107)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(154, 528, 67, 107)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(283, 528, 65, 107)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(416, 528, 91, 107)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(537, 566, 99, 69)
        self.punchFrames.append(self.image)
        self.image = self.spritesheet.getImage(670, 566, 87, 69)
        self.punchFrames.append(self.image)

    def showIdle(self):
        if self.index >= len(self.idleFrames):
            self.index = 0
        self.image = self.idleFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1

    def showWalking(self):
        if self.index >= len(self.walkingFrames):
            self.index = 0
        self.image = self.walkingFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1

    def showPunch(self):
        if self.index >= len(self.punchFrames):
            self.index = 0
        self.image = self.punchFrames[self.index]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.index += 1
