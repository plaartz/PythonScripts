# Using spotify API get current soundtrack

import sys
import os
import json
import webbrowser
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
from time import sleep

# export SPOTIPY_CLIENT_ID='41c4856f7e8f46348805553646e68ebc'
# export SPOTIPY_CLIENT_SECRET='e467d32845b74e21bf840259287e3b91'
# export SPOTIPY_REDIRECT_URI='http://google.com/'

#Get Username from terminal laartz.porter
username = sys.argv[1]
#Prompt user permission
token = util.prompt_for_user_token(username, 'user-read-currently-playing')




#Create spotify object
sp = spotipy.Spotify(auth=token)

pastSongName = None
Playback = sp.current_user_playing_track()
#print(json.dumps(Playback, sort_keys=True, indent=4))
while True :
    try :
        Playback = sp.current_user_playing_track()
        artistName = Playback['item']['album']['artists'][0]['name']
        songName = Playback['item']['name']
        albumImg = Playback['item']['album']['images'][1]['url']
 
        if songName != pastSongName :
            print(artistName)
            print(songName)
            print(albumImg)

            pastSongName = songName
    except :
        print("Unexpected Error")
    sleep(1)
    
print(json.dumps(artistName, sort_keys=True, indent=4))

