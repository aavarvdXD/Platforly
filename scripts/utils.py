import os

import pygame as pg

BASE_IMG_PATH = "res/sprites/"

def loadImg(path):
    img = pg.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def loadImgs(path):
    imgs = []
    for imgName in sorted(os.listdir(BASE_IMG_PATH + path)):
        imgs.append(loadImg(path + "/" + imgName))
    return imgs