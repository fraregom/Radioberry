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
play_song = ""
on = ""
cont = True
for i in results['tracks']['items']:
    if cont == True:
        play_song = str(i["uri"])
        on = unicodedata.normalize("NFKD",i['name']).encode("ascii","ignore")+" de "+ unicodedata.normalize("NFKD",i["artists"][0]["name"]).encode("ascii","ignore") 
        cont = False
    print i['name'],"de",i["artists"][0]["name"],"\n"#i["external_urls"]["spotify"]+"\n"#nombre,artista,url cancion

audio = spotify.AlsaSink(session)
track = session.get_track(play_song)
track.load()
session.player.load(track)
session.player.play()
print "\n\n","########## Estas escuchando ",on,"##########"
raw_input()


