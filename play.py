import os, time
import subprocess
print("Hola")
print("Playing...")

#play = os.sys("livestreamer hlsvariant://multimedioshls-i.akamaihd.net/hls/live/223118/57828478001/master.m3u8 best --player omxplayer --fifo player-passthrough hls")
cmd = "livestreamer"
cmd2 ="livestreamer hls://multimedioshls-i.akamaihd.net/hls/live/223118/57828478001/master/720/index.m3u8 best --player omxplayer --fifo --player-passthrough hls"
cmd3 = cmd2.split(" ")
process = subprocess.Popen(cmd3)
#process.communicate()
time.sleep(45)
print("Terminar ")
#pid_ = process.pid
#os.system('kill -9 %s'%pid_)
process.terminate()
#process.wait()
print process.returncode
