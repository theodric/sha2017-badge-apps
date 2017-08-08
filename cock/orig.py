#based on Working Clock
import easyrtc
import ugfx
import badge
import time
import wifi
import appglue
import urandom


badge.init()
ugfx.init()
wifi.init()
easyrtc.configure()

ugfx.clear(ugfx.WHITE)
ugfx.string(0,0,"Hey look at my c**ck","PermanentMarker24",ugfx.BLACK)
t = easyrtc.string()
n = urandom.getrandbits(2)

ugfx.box(120, 40, 120, 60, ugfx.BLACK)
ugfx.area(120, 40, 120, 60, ugfx.BLACK)
#ugfx.string(130, 50, t, "PermanentMarker36", ugfx.WHITE)
ugfx.string(100, 20, str(n), "PermanentMarker36", ugfx.WHITE)

ugfx.flush()
time.sleep(20)
appglue.home()
