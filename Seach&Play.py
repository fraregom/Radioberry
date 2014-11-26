# -*- coding: utf-8 -*-
import spotipy
import spotify
import unicodedata

session = spotify.Session()
session.login('USER','PASSWORD')
while True:
    session.process_events()
    print "Conectando......."
    if session.connection.state == 1:
        break
    
spotipy = spotipy.Spotify()
print "\n\n","-----------------------------------------------------------------","\n\n"
cancion=raw_input("Ingresa el nombre de la cancion que quieres escuchar: ")
print "\n\n"
results = spotipy.search(cancion, limit=10)
songs = {}
cont = 1
for i in results['tracks']['items']:
    on = unicodedata.normalize("NFKD",i['name']).encode("ascii","ignore")+" de "+ unicodedata.normalize("NFKD",i["artists"][0]["name"]).encode("ascii","ignore")
    songs[str(cont)] = {"play_song":str(i["uri"]),"name":on,"image":i['album']['images'][1]['url']}
    print str(cont)+".-"+ i['name'],"de",i["artists"][0]["name"]
    cont += 1
play = raw_input("\n\n¿Cual Quieres escuchar?: ")
audio = spotify.AlsaSink(session)
track = session.get_track(songs[play]["play_song"])
track.load()
session.player.load(track)
session.player.play()
print "\n\n","########## Estas escuchando ",songs[play]["name"],"##########"
print songs[play]["image"]
raw_input()


