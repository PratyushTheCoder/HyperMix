from os import path, getcwd, chdir
import json


config_file=getcwd()+"/hypermix.json"

def load_database():
    if path.exists(config_file):
        with open(config_file,"r+") as database:
            data=json.load(database)
            version=data['version']
            username=data['username']
            music_dir=data['music_dir']
        chdir(music_dir)
        with open("./player.json","r+") as lp:
            lastplayed=json.load(lp)['lastplayed']
            lp.close()
    else:
        with open(config_file, "w+") as database:
            print("Database not found, creating one...\n")
            username=input("Please enter your name: ")
            music_dir=input("Please enter the path for your music directory: ")
            data_template={"version":"1.0.0","music_dir":f"{music_dir}","username":f"{username}"}
            json.dump(data_template,database)
            database.close()
        chdir(music_dir)
        with open("./player.json","w+") as lp:
            lastplayed={"last_played":""}
            json.dump(lastplayed,lp)
            lp.close()
            print("Database created, Run the program again to continue")
        quit()
    return music_dir, version, username, lastplayed

