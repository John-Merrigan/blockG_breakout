import vlc
from random import randint


def playMusic(): #randomly play song
    a = (randint(0,9))
    if a == 1:
        p = vlc.MediaPlayer("file:///Users/admin/Desktop/Jimmy Cliff-Breakout.mp3")
        p.play()
    elif a == 2:
        p = vlc.MediaPlayer("file:///Users/admin/Desktop/Break On Through.mp3")
        p.play()
    elif a ==3:
         p = vlc.MediaPlayer("file:///Users/admin/Desktop/03 Love Story.m4a")
         p.play()
    elif a == 4:
        p = vlc.MediaPlayer("file:///Users/admin/Desktop/1-09 Fly Like an Eagle.mp3")
        p.play()
    elif a == 5:
        p = vlc.MediaPlayer("file:///Users/admin/Desktop/Break On Through.mp3")
        p.play()
    else:
        p = vlc.MediaPlayer("file:///Users/admin/Desktop/Hucci x GameFace - The Leaves Are Brown-[www.KlubowaMuza.net].mp3")
        p.play()
