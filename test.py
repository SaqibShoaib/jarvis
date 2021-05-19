# import os
# music_dir = 'C:\\Users\\Muhammad Saqib\\Music\\music'
# songs = os.listdir(music_dir)
# for song in songs:
#     song = song.split()
#     for i in song[0:4]:
#         print(i,end=" ")
#     print()
# #  os.startfile(os.path.join(music_dir, 'playlists\\classic.wpl'))
from datetime import datetime
time = datetime.now().strftime("%I:%M:%S:%p")
print(time)