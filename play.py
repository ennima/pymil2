import os
print("Hola")
print("Playing...")

play = os.sys("livestreamer hlsvariant://multimedioshls-i.akamaihd.net/hls/live/223118/57828478001/master.m3u8 best --player omxplayer --fifo player-passthrough hls")
if(play == 0):
	print "Mamo"
else:
	print "Cool"