# -*- coding: utf-8 -*-
import spotipy               # Se importa spotipy, esta libreria nos permite hacer busquedas en la base de datos de spotify
import spotify               # Se importa spotify, esta libreria nos permite construir nuestro cliente ya que nos facilita la reproducion de musica.
import unicodedata           # Esta libreria tiene como funcion la limpieza de strings de cualquier caracter no permitido en algun titulo 

session = spotify.Session()        #siempre en este programa se debe crear una session, luego el cliente mismo la recordara y hara el tramite mas rapido
session.login('USER','PASSWORD')   #se nos solicitara nuestro usuario de spotify, ya que sin esta funcion no nos permitiria la reproducion de musica
while True:
    session.process_events()
    print "Conectando......."
    if session.connection.state == 1:  # cuando se cumpla dicha condicion, efectivamente estaremos conectados y listos para usar el cliente
        break
    
spotipy = spotipy.Spotify()
print "\n\n","-----------------------------------------------------------------","\n\n"
cancion=raw_input("Ingresa el nombre de la cancion que quieres escuchar: ")     # se crea un input cuya funcion es obtener el nombre de la cancion que se quiere escuchar
print "\n\n"
results = spotipy.search(cancion, limit=10)   # en este caso se implemento que la busqueda nos entregase solo 10 canciones, obviamente son las con mayores coincidencias                                                
songs = {}                                    # ordenadas de modo mejor a peor opcion
cont = 1
for i in results['tracks']['items']:
    on = unicodedata.normalize("NFKD",i['name']).encode("ascii","ignore")+" de "+ unicodedata.normalize("NFKD",i["artists"][0]["name"]).encode("ascii","ignore")
    songs[str(cont)] = {"play_song":str(i["uri"]),"name":on,"image":i['album']['images'][1]['url'],"ID":i['name']}
    print str(cont)+".-"+ i['name'],"de",i["artists"][0]["name"] # en esta parte del codigo mas que nada se obtiene informacion valiosa como el nombre
    cont += 1                                                     # de la cancion, del artista y su cover de album, se almacena todo en un diccionario 
    
play = raw_input("\n\n¿Cual Quieres escuchar?: ")    # este input nuevamente nos preguntara cual cancion queremos escuchar, rellenaremos este campo con el numero de la cancion
audio = spotify.AlsaSink(session)                    # para poder escuchar las canciones se utiliza ALSA, es un software de sonido presente en sistemas linux
track = session.get_track(songs[play]["play_song"])
track.load()
session.player.load(track)
session.player.play()     # se procede con la reproducion
print "\n\n","########## Estas escuchando ",songs[play]["name"],"##########"
# se entrega el nombre de la cancion y el artista a  su vez su respectivo cover 

resource = urllib.urlopen(songs[play]["image"])
output = open(songs[play]["ID"]+".jpg","wb")
output.write(resource.read())
output.close()
raw_input()

 

