import os
import subprocess
print("Hola")
print("Playing...")

#play = os.sys("livestreamer hlsvariant://multimedioshls-i.akamaihd.net/hls/live/223118/57828478001/master.m3u8 best --player omxplayer --fifo player-passthrough hls")
cmd = "livestreamer hlsvariant://multimedioshls-i.akamaihd.net/hls/live/223118/57828478001/master.m3u8 best --player omxplayer --fifo player-passthrough hls"
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
process.wait()
print process.returncode