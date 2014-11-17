import spotipy
spotify = spotipy.Spotify()

name = raw_input("Ingrese el nombre del artista a buscar: ")
results = spotify.search(q='artist:' + name, type='artist')
print "El Artista(s) se llama(n):",results["artists"]["items"][0]["name"]
print "Imagen Referencial:", results["artists"]["items"][0]["images"][0]["url"]
generos = " "
for a in (results["artists"]["items"][0]["genres"]):
    generos += a + " "
print "El genero del artista(s) es:" ,generos 
print "Las canciones favoritas de la gente:"
results = spotify.search(q=str(name), limit=10)
for i, t in enumerate(results['tracks']['items']):
    print ' ', (i+1), t['name']
