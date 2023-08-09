import os 
dir_list = os.listdir("gameneeds/")
for i in dir_list:
    dir_liste = os.listdir("gameneeds/" + i + "/")
    for s in dir_liste:
	    os.system("ffmpeg -i gameneeds/" + i + "/" + s + " -vf scale=64:64,setsar=1:1  gameneeds/" + i + "/new_" + s)
