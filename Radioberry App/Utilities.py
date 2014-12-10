# -*- coding: utf-8 -*-
import spotipy
import spotify
import unicodedata
import urllib
import Image
import os
cox = 1
def connect_spotify(session,cox):
        if cox == 1:
                print "Conectando......."
                while True:
                        session.process_events()
                        if session.connection.state == 1:
                                print "Conectado"
                                break
        else:
                session.login('USER','PASSWORD')
                print "Conectando......."
                while True:
                        session.process_events()
                        if session.connection.state == 1:
                                print "Conectado"
                                break

	return

spotipy = spotipy.Spotify()
def search_music(Entrada,session):
    
    connect_spotify(session,cox)
    results = spotipy.search(Entrada, limit=20)
    songs = {}
    for i in results['tracks']['items']:
        albumname=i['album']['name']
        name = unicodedata.normalize("NFKD",i['name']).encode("ascii","ignore")
        artist = unicodedata.normalize("NFKD",i["artists"][0]["name"]).encode("ascii","ignore")
        songs[name] = {"play":str(i["uri"]),"artista":artist,"imagen":i['album']['images'][1]['url'],'preview_url':i["preview_url"]}
    return songs

def search_artist(Entrada,session):
    connect_spotify(session,cox)
    artist = {}
    results = spotipy.search(q='artist:' + Entrada, type='artist')
    imagen_artist = results["artists"]["items"][0]["images"][0]["url"]
    names = str(results["artists"]["items"][0]["name"])
    generos = " "
    for a in (results["artists"]["items"][0]["genres"]):
        generos += a + " "
    results = spotipy.search(q=str(Entrada), limit=20)
    songs = {}
    for t in results['tracks']['items']:
        name = unicodedata.normalize("NFKD",t["name"]).encode("ascii","ignore")
        uri = unicodedata.normalize("NFKD",t["uri"]).encode("ascii","ignore")
        image = t["album"]["images"][1]["url"]
        songs[name] = {"artista":names,"play":uri,"imagen":image,'preview_url':t["preview_url"]}
    dic={}
    dic["imagen"]=imagen_artist
    dic["generos"]=generos
    dic["top"]=songs
    artist[names] = dic
    return tuple((artist,names))

def search_album(Entrada,session):
    connect_spotify(session,cox)
    results = spotipy.search(Entrada)
    songs = {}
    for a in results['tracks']["items"]:
        image = a["album"]["images"][1]["url"]
        
        name = unicodedata.normalize("NFKD",a["name"]).encode("ascii","ignore")
        uri = unicodedata.normalize("NFKD",a["uri"]).encode("ascii","ignore")
        songs[name] = {"artista":a["artists"][0]["name"],"uri":uri,"cover":image,'preview_url':a["preview_url"]}
    return songs 

def cover(name,image):
	
	resource = urllib.urlopen(image)
	output = open(name+".jpg","wb")
	output.write(resource.read())
	output.close()
	im = Image.open(name+'.jpg')
	im.save(name+'.gif')
	os.remove(name+'.jpg')
	return
	

def play_music(name,image,song,session):
	connect_spotify(session,cox)
	cover(name,image)
	audio = spotify.AlsaSink(session)
	track = session.get_track(song)
	track.load()
	session.player.load(track)
	session.player.play()
	return

def play_radio(name):
	print name
	#os.system("sudo sh pifmplay "+"'"+name+"'"+" 88.5 playstream")
	return
    
