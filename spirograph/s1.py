#based on Working Clock without permission
#come at me, bro.
import ugfx
import badge
import time
import random


badge.init()
ugfx.init()

def draw():
    ugfx.clear(ugfx.WHITE)

    ugfx.line(0, 0, 180, 100, ugfx.BLACK)


while True:
    draw()
