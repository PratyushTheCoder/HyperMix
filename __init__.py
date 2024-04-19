from os import  chdir ,mkdir, listdir
from player import play
from config import load_database
from time import strftime

hour=int(strftime('%H'))
if hour<12:
    TIME_OF_DAY="Morning"
elif hour>=12 and hour<18:
    TIME_OF_DAY="Afternoon"
else:
    TIME_OF_DAY="Evening"

database=load_database()
MUSIC_DIR=database[0]
VERSION=database[1]
USERNAME=database[2]
LAST_PLAYED=database[3]

print(f"""     \n HyperMix({VERSION}) - Music for your CLI\n
        Good {TIME_OF_DAY}, {USERNAME}
""")

options=[
    'Select a playlist to play from',
    f'Play from last played ({LAST_PLAYED})',
    'Quit'

]
i=0
print("\nPlease select a option to continue...\n")
for option in options:
   i+=1
   print(f"{i}. {option}") 

query=int(input("\nChoice: "))
playlist=listdir()
remove=[
    'player.json',
    'termix.log',
    'ignore'
]
for r in remove:
    playlist.remove(r)

if query==1:
    i=0
    print()
    for list in playlist:
        i+=1
        print(f"{i}. {list}")
    query=int(input("\nChoice: "))
    query-=1
    chdir(playlist[query])
    print("""\nControls:
Press 'p' or 'space_bar' to pause
Press 'r' or 'space_bar' to resume
Press 'n' or 'enter_key' to change song
Press 'q' or 'esc_key' to quit                             \n
""")
    for songs in listdir():
        play(songs)

else:
    print("\nBye...\n")