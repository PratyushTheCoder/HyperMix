from pygame import mixer

VOLUME=float(1)

mixer.init()
mixer.music.set_volume(VOLUME)

def play(song):
    try:    
        if song.split('.')[1]=="mp3":
            try:
                mixer.music.load(song)
            except Exception as e:
                print(f"\nError while trying to play {song.split('.')[0]}")
            print(f"\nPlaying: {song}\n")
            mixer.music.play()
            while True:
                query=input("Command: ")
                if query=='p':
                    mixer.music.pause()
                elif query=='r':
                    mixer.music.unpause()
                elif query=='n':
                    break
                else:
                    print("\nBye... \n")
                    quit(0)
                pass
        else:
            print(f"\nFile type {song.split('.')[1]} not supported. Skipping {song.split('.')[0]}...\n")
    except Exception as e:
        print("Error")