#based on Working Clock without permission
#come at me, bro.
import easyrtc
import ugfx
import badge
import time
import wifi
import random

badge.init()
ugfx.init()
wifi.init()
easyrtc.configure()

first = ['Holy', 'Shitty', 'Jizzy', 'Still', 'Fucking', 'Jaevla', 'Moronic'];
second = [' wanking ', ' shagging ', ' fucking ', ' hacking ', ' cunting ', ' unwashed ', 'Mac-using']
third = ['assballs!', 'dick!', 'anyway!', 'twat!', 'NetBSD!', 'buggery!', 'Mac users']

def cuss():
    t = easyrtc.string()
    ugfx.clear(ugfx.WHITE)

#ugfx.string(x, y, string, font, colour)
    ugfx.string(10, 5, str(random.choice(first)), "PermanentMarker36", ugfx.BLACK)
    ugfx.string(30, 30, str(random.choice(second)), "PermanentMarker36", ugfx.BLACK)
    ugfx.string(100, 55, str(random.choice(third)), "PermanentMarker36", ugfx.BLACK)
#    ugfx.string(110, 85, str(herp), "PermanentMarker22", ugfx.BLACK)
    ugfx.string(30, 85, " it's ", "PermanentMarker22", ugfx.BLACK)
    ugfx.string(140, 85, t, "PermanentMarker36", ugfx.BLACK)

    ugfx.flush()
    time.sleep(3)


while True:
    cuss()
