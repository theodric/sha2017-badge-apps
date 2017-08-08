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


first = ['Holy', 'Shitty', 'Jizzy', 'Still', 'Fucking', 'Jaevla', 'Moronic'];
second = [' wanking ', ' shagging ', ' fucking ', ' hacking ', ' cunting ', ' unwashed ', 'Mac-using']
third = ['Assballs!', 'Dick!', 'Anyway!', 'Twat!', 'NetBSD!', 'Buggery!', 'Mac users']

def cuss():
##    t = easyrtc.string()
    ugfx.clear(ugfx.WHITE)
    one = str(random.choice(first))
    two = str(random.choice(second))
    three = str(random.choice(third))

    len1 = ugfx.get_string_width(one,"Roboto_BlackItalic24")
    len2 = ugfx.get_string_width(two,"PermanentMarker36")
    len3 = ugfx.get_string_width(three,"Roboto_BlackItalic24")

    ugfx.string_box(90,0,len1,24, one, "Roboto_BlackItalic24", ugfx.BLACK, ugfx.justifyCenter)
    ugfx.string_box(40,25,len2,36, two, "PermanentMarker36", ugfx.BLACK, ugfx.justifyCenter)
    ugfx.string_box(90,63,len3,34, three, "Roboto_BlackItalic24", ugfx.BLACK, ugfx.justifyCenter)

###ugfx.string(x, y, string, font, colour)    
    #ugfx.string(20, 5, str(random.choice(first)), "Roboto_BlackItalic24", ugfx.BLACK, ugfx.justifyCenter)
    #ugfx.string(30, 20, str(random.choice(second)), "PermanentMarker36", ugfx.BLACK)
    #len = ugfx.get_string_width(str(random.choice(second)),"PermanentMarker36")
    #ugfx.line(25, 57, 64 + len, 57, ugfx.BLACK)
    #ugfx.line(140 + len, 52, 140 + len, 70, ugfx.BLACK)
    #ugfx.string(120, 60, str(random.choice(third)), "Roboto_BlackItalic24", ugfx.BLACK)
    #ugfx.string(30, 95, " it's ", "PermanentMarker22", ugfx.BLACK)
##    ugfx.string(140, 95, t, "PermanentMarker36", ugfx.BLACK)

    ugfx.flush()
    time.sleep(3)

while True:
    cuss()
