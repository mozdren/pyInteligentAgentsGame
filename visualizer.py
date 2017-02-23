import pygame
from pygame.locals import *
import time

testovaci = [
    "ooooooooooo",
    "ottt  * ffo",
    "ott  ** ffo",
    "ot~  * fffo",
    "o~~  *  ffo",
    "o~~~**  tfo",
    "oooo*~~~~~o",
    "offo* ~~~~o",
    "offf*  ~~to",
    "offo  ~~tto",
    "ooooooooooo",
    "           ",
    "           ",
    "      p    ",
    "           ",
    "           ",
    "           ",
    "           ",
    "    p      ",
    "           ",
    "           ",
    "           "
]

class Visualizer(object):
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((330,330), pygame.HWSURFACE)
        self.grass = pygame.image.load("trava.png").convert()
        self.tree = pygame.image.load("strom.png").convert()
        self.rock = pygame.image.load("skala.png").convert()
        self.road = pygame.image.load("cesta.png").convert()
        self.floor = pygame.image.load("podlaha.png").convert()
        self.water = pygame.image.load("voda.png").convert()
        self.player = pygame.image.load("player.png").convert_alpha()
        self.running = True
    def visualize(self,data):
        for y in xrange(11):
            for x in xrange(11):
                ox = x*30
                oy = y*30
                if data[y][x] == " ":
                    self.display.blit(self.grass,(ox,oy))
                elif data[y][x] == "t":
                    self.display.blit(self.tree,(ox,oy))
                elif data[y][x] == "o":
                    self.display.blit(self.rock,(ox,oy))
                elif data[y][x] == "~":
                    self.display.blit(self.water,(ox,oy))
                elif data[y][x] == "f":
                    self.display.blit(self.floor,(ox,oy))
                elif data[y][x] == "*":
                    self.display.blit(self.road,(ox,oy))
                else:
                    self.display.blit(self.rock,(ox,oy))
        if len(data)>11:
            for y in xrange(11):
                for x in xrange(11):
                    ox = x*30
                    oy = y*30
                    if data[y+11][x] == "p":
                        self.display.blit(self.player,(ox,oy))
        #self.display.blit(self.player,(5*30,5*30))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
    def __enter__(self):
        return self
    def __exit__(self, otype, value, traceback):
        pygame.quit()

if __name__ == "__main__":
    with Visualizer() as vis:
        while vis.running:
            vis.visualize(testovaci)
            time.sleep(0.1)
