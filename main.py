import time

from pypresence import Presence

rpc = Presence("878561116630953985")
rpc.connect()
rpc.update(state='Chillin Around',
           details='Hishaam do be trash tho',
           large_image='epic',
           buttons=[{'label':'Idk Discord Server', 'url':'https://discord.gg/vFrsNYxz3G'}])

print('Status has now been updated. The app will not stay open forever cause of pyinstaller')

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("Bye!")


countdown(100000)
