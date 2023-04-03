# Desafio 021

import vlc # importa o vlc para tocar a música
import time
p = vlc.MediaPlayer("March-comes-in-like-a-lion-opening-3.mp3")
p.play()
time.sleep(60)
p.stop