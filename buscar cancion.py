import spotipy
sp = spotipy.Spotify()

q=raw_input("ingrese la cancion que quiere buscar: ")
results = sp.search(q, limit=10)
#print results
for i in results['tracks']['items']:
    print i['name'],"de",i["artists"][0]["name"],"\n",i["external_urls"]["spotify"]+"\n"#nombre,artista,url cancion
raw_input()


