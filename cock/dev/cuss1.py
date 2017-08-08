#based on Working Clock
##import easyrtc
import ugfx
import badge
import time
##import wifi
#import appglue
#import urandom
import random


badge.init()
ugfx.init()
##wifi.init()
##easyrtc.configure()


first = ['Holy', 'Shitty', 'Jizzy', 'Still', 'Fucking', 'Jaevla'];
second = [' wanking ', ' shagging ', ' fucking ', ' hacking ', ' cunting ', ' unwashed ']
third = ['assballs!', 'dick!', 'anyway!', 'twat!', 'NetBSD!', 'buggery!']

def cuss():
    ugfx.clear(ugfx.WHITE)
    #ugfx.string(0,0,"Hey, look at my c*ock!","PermanentMarker24",ugfx.BLACK)
##    t = easyrtc.string()
#    n1 = random.getrandbits(2)
#    n2 = random.getrandbits(2)
#    n3 = random.getrandbits(2)
    #herp = len(first)
    herp = str(random.choice(first))

#    ugfx.string(50, 10, str(first[n1]), "PermanentMarker24", ugfx.BLACK)
#    ugfx.string(70, 35, str(second[n1]), "PermanentMarker24", ugfx.BLACK)
#    ugfx.string(90, 60, str(third[n1]), "PermanentMarker24", ugfx.BLACK)
    ugfx.string(30, 5, str(random.choice(first)), "PermanentMarker36", ugfx.BLACK)
    ugfx.string(50, 30, str(random.choice(second)), "PermanentMarker36", ugfx.BLACK)
    ugfx.string(100, 55, str(random.choice(third)), "PermanentMarker36", ugfx.BLACK)
#    ugfx.string(110, 85, str(herp), "PermanentMarker24", ugfx.BLACK)
    ugfx.string(110, 85, " it's ", "PermanentMarker24", ugfx.BLACK)
    ugfx.string(130, 50, t, "PermanentMarker36", ugfx.BLACK)

    ugfx.flush()
    time.sleep(3)
    cuss()

cuss()
#appglue.home()
