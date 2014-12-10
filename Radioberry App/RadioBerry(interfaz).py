from Tkinter import *
from Utilities import *
import spotipy
import spotify
import unicodedata
import urllib
import ImageTk

#Crear Ventana
ventana = Tk()
ventana.geometry('1024x700+50+50')
ventana.title('Radio Berry')

cox=[]
Radios=['']
lista_imagenes = ["LogoG.gif"]
lista_radio = []
DicPlay=dict()
DicBuscar=dict()
session = spotify.Session()
session.login('USER','PASSWORD')

def Buscar():
	if Radios[-1] == "Cancion":		
		Datos=search_music(str(Entrada.get()),session)
		for llave,valor in Datos.items():	
			lstBuscar.insert(END,llave+' ---> '+valor['artista'])
			DicBuscar[llave]=valor
			#play, artista, imagen
		
	
	elif Radios[-1]=='Album':		
		Datos=search_album(str(Entrada.get()),session)
		for llave,valor in Datos.items():
	
			lstBuscar.insert(END,str(llave)+' ---> '+valor['artista'])
			DicBuscar[str(llave)]={'play':valor['uri'],'artista':valor['artista'],'imagen':valor['cover']}
			
		
	elif Radios[-1]=='Artista':
		Datos = search_artist(str(Entrada.get()),session)
		canciones = Datos[0][Datos[1]]["top"]
		for a,b in canciones.items():
			lstBuscar.insert(END,a+' ---> '+b['artista'])
			DicBuscar[a]=b
	Entrada.set('')
	return
	
def btnMenosPlay():
	index=lstPlay.curselection()
	nombre=lstPlay.get(index).split(' ---> ')
	del DicPlay[nombre[0]]
	lstPlay.delete(lstPlay.curselection())
def btnMenosBuscar():
	index=lstBuscar.curselection()
	nombre=lstBuscar.get(index).split(' ---> ')[0]
	del DicBuscar[nombre]
	lstBuscar.delete(lstBuscar.curselection())
def btnMas():
	index=lstBuscar.curselection()
	lstPlay.insert(END,lstBuscar.get(index))
	nombre=lstBuscar.get(index).split(' ---> ')[0]
	DicPlay[nombre]=DicBuscar[nombre]
	del DicBuscar[nombre]
	lstBuscar.delete(index)
def RadioA():
	Radios.append('Artista')
	return Radios	
def RadioAl():
	Radios.append('Album')
	return Radios	
def RadioC():
	Radios.append('Cancion')
	return Radios
	
def btnPlay():
	index=lstPlay.curselection()
	Actual=lstPlay.get(index)
	nombre=Actual.split(' ---> ')[0]
	artista=Actual.split(' ---> ')[1]
	Info=DicPlay[nombre] #play(link cancion), artista(nombre), imagen(url album)
	play_music(nombre,Info['imagen'],Info['play'],session)
	lista(nombre,lista_imagenes)
	cambio_imagen(lista_imagenes)
	Info2=search_artist(artista,session)
	Album=search_music(nombre,session)#####
	Info2[0][artista]['generos']
	lstInfo.insert(END,'Cancion: '+nombre)
	lstInfo.insert(END,'Artista: '+artista)
	lstInfo.insert(END,'Genero : '+Info2[0][artista]['generos'])
	return 
	#items = map(int, list.curselection()) 

def lista(nombre,lista_imagenes):
        lista_imagenes.append(str(nombre)+".gif")
        return lista_imagenes

def cambio_imagen(lista_imagenes):
        image = lista_imagenes[-1]
        img2 = ImageTk.PhotoImage(file = image)
        lblimg.configure(image = img2)
        lblimg.image = img2
        return

def iniciar_radio(lista_radio):
        play_radio(lista_radio[-1])
        return
        
                        
image = lista_imagenes[-1]
img = ImageTk.PhotoImage(file = image)
lblimg=Label(ventana,image=img)#.place(x=360,y=181)#x=360,y=181
lblimg.pack(side = "bottom", fill = "both", expand = "yes")


#LabelTxt------>Palabras o Frases
lblBerry=Label(text='Radio Berry',font=('Arial',48)).place(x=200,y=40)


#StringVar------->Barra para escribir
Entrada=StringVar()
Entrada.set('')
txtEntrada=Entry(ventana,text=Entrada,width=25,font=('Arial',12)).place(x=590,y=42)


#RadioButton----->Botones redondos
seleccion=IntVar()
rbtnArtista=Radiobutton(ventana,command=RadioA,variable=seleccion,text='Artista  ', value=1).place(x=850,y=35)
rbtnAlbum=Radiobutton(ventana,command=RadioAl,variable=seleccion,text='Album  ', value=2).place(x=850,y=65)
rbtnCancio=Radiobutton(ventana,command=RadioC,variable=seleccion,text='Cancion', value=3).place(x=850,y=95)



#Button------>Boton de Busqueda
btnBuscar=Button(ventana,text='Buscar',width=22,font=('Arial',12),cursor='center_ptr', 
command=Buscar,activebackground='grey').place(x=596,y=92)

#ListBox----->Listado de Canciones
lstPlay=Listbox(ventana,width=35,height=26)
lstBuscar=Listbox(ventana,width=35,height=26)
lstInfo=Listbox(ventana,width=30,height=3,font=('Arial',14))

def Reproduce():
	session.player.play()
	return
def btnPausa():
	session.player.pause()
	return
def btnStop():
	session.logout()
	cox.append(0)
	return
def btnBack():
	session.player.play()
	return
def btnForward():
	return

def Radio():  ###############
	index=lstPlay.curselection()
	Actual=lstPlay.get(index)
	nombre=Actual.split(' ---> ')[0]
	artista=Actual.split(' ---> ')[1]
	Info=DicPlay[nombre]
	cover(nombre,Info["imagen"])
	lista(nombre,lista_imagenes)
	cambio_imagen(lista_imagenes)
	lista_radio.append(Info["preview_url"])
	iniciar_radio(lista_radio)
	Info2=search_artist(artista,session)
	Info2[0][artista]['generos']
	lstInfo.insert(END,'Cancion: '+nombre)
	lstInfo.insert(END,'Artista: '+artista)
	lstInfo.insert(END,'Genero : '+Info2[0][artista]['generos'])
    
#ImageButton
Mas=PhotoImage(file='mas.gif')
ibtnMas=Button(ventana,image=Mas,width=30,height=25,command=btnMas,cursor='center_ptr').place(x=710,y=190)

Menos=PhotoImage(file='menos.gif')
Reproduce=PhotoImage(file='play.gif')
ibtnMenosPlay=Button(ventana,image=Menos,command=btnMenosPlay,width=30,cursor='center_ptr',height=25).place(x=32,y=190)
ibtnMenosBuscar=Button(ventana,image=Menos,command=btnMenosBuscar,width=30,cursor='center_ptr',height=25).place(x=950,y=190)
ibtnCargar=Button(ventana,text='Reproducir!',command=btnPlay,fg='green',font=('Arial',12),cursor='center_ptr').place(x=100,y=190)

Pausa=PhotoImage(file='pause.gif')
ibtnPausa=Button(ventana,image=Pausa,command=btnPausa,width=30,height=25,cursor='center_ptr').place(x=550,y=510)

stop=PhotoImage(file='stop.gif')
ibtnStop=Button(ventana,image=stop,command=btnStop,width=30,height=25,cursor='center_ptr').place(x=430,y=510)


ibtnBack=Button(ventana,image=Reproduce,command=btnBack,width=30,height=25,cursor='center_ptr').place(x=490,y=510)#

radio=PhotoImage(file="Minilogo.gif")
ibtnradio=Button(ventana,image=radio,command=Radio,width=70,height=70,cursor='center_ptr').place(x=80,y=40)

#listbox x,y
lstPlay.place(x=35,y=220)
lstBuscar.place(x=710,y=220)
lstInfo.place(x=360,y=570)



ventana.mainloop()
#10.112.8.176 IP raspberry ciac

