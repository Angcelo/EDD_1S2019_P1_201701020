import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_ENTER
import serpiente
import Usuarios
import pilaboca
import Puntaje
import os
from random import randint, uniform,random

Nombre=""
dificultad=0
User=Usuarios.usuarios()	
Records=Puntaje.lista()

class Jugar():
	def __init__(self):
		global Nombre
		global User
		global dificultad
		activado=False
		tipo=0
		if  Nombre=="":
			screen = curses.initscr()
			height = 10
			width=50
			pos_y=0
			pos_x=0
			window = curses.newwin(height,width,pos_y,pos_x)
			window.keypad(True)
			curses.curs_set(0)
			curses.echo()
			window.border(0)
			window.nodelay(False)
			window.addstr(3,5,"Introduzca un nombre, enter para continuar")
			window.addstr(4,5," ")
			key=window.getkey()
			Nombre=""
			while key!="\n":
				Nombre=Nombre+str(key)
				key=window.getkey()
				pass
			User.insertar(Nombre)
			window=curses.endwin()
			pass
		screen2 = curses.initscr()
		height = 25
		width=50
		pos_y=0
		pos_x=0
		espx=0
		espy=0
		window = curses.newwin(height,width,pos_y,pos_x)
		window.keypad(True)
		curses.curs_set(0)
		curses.noecho()
		window.border(0)
		window.nodelay(True)
		snake=serpiente.ListaDoble()
		comida=pilaboca.Pila()
		snake.insertar_inicio(3,2)
		snake.insertar_inicio(2,2)
		snake.insertar_inicio(1,2)
		window.addstr(0,18,"Nombre:"+Nombre)
		key=KEY_RIGHT
		pos_x=snake.obtener_pos(2,1)
		pos_y=snake.obtener_pos(2,2)
		for x in range(0,snake.get_indice()+1):
			window.addch(snake.obtener_pos(x,2),snake.obtener_pos(x,1),'#')
			pass
		while key!=27:
			window.addstr(0,1,"Puntaje:"+str(comida.get_puntaje())+"-")
			if(dificultad==1):
				for x in range(0,6):
					window.addstr(5+x,15,"|")
					window.addstr(5+x,35,"|")
					window.addstr(15+x,15,"|")
					window.addstr(15+x,35,"|")
					pass
			if activado==False:
				espx=randint(2,48)
				espy=randint(2,23)
				if dificultad==1:
					while (espx==15 or espx==35) and (espy==5 or espy==6 or espy==7 or espy==8 or espy==9 or espy==10 or espy==15 or espy==16 or espy==17 or espy==18 or espy==19 or espy==20):
						espx=randint(2,48)
						espy=randint(2,23)
						pass
					pass
				espcual=randint(0,9)
				if espcual>=8:
					window.addch(espy,espx,'*')
					activado=True
					tipo=2
				else:
					window.addch(espy,espx,'+')
					activado=True
					tipo=1
					pass
				pass
			window.timeout(100)
			keystroke=window.getch()
			if keystroke==KEY_RIGHT and key==KEY_LEFT:
				key=KEY_LEFT
			elif key==KEY_RIGHT and keystroke==KEY_LEFT:
				key=KEY_RIGHT
			elif keystroke==KEY_UP and key==KEY_DOWN:
				key=KEY_DOWN
			elif keystroke==KEY_DOWN and key==KEY_UP:
				key=KEY_UP
			elif keystroke is not -1:
				if keystroke==KEY_RIGHT or keystroke==KEY_LEFT or  keystroke==KEY_UP or keystroke==KEY_DOWN or keystroke==27:
					key=keystroke
					pass
				pass
			for x in range(0,snake.get_indice()+1):
				window.addch(snake.obtener_pos(x,2),snake.obtener_pos(x,1),' ')
				pass
			if key==KEY_RIGHT:
				pos_x=pos_x+1
			elif key==KEY_LEFT:
				pos_x=pos_x-1
			elif key==KEY_UP:	
				pos_y=pos_y-1
			elif key==KEY_DOWN:
				pos_y=pos_y+1
				pass
			if(comida.get_puntaje()==15 and dificultad==0):
				dificultad=1
				window=curses.endwin()
				Jugar()
				pass
			elif(comida.get_puntaje()==15 and dificultad==1):
				Records.encolar(15+comida.get_puntaje(),Nombre)
				snake.graficar()
				comida.graficar()
				key=27
			snake.cambiar_posicion()
			snake.editar_ultimo(pos_x,pos_y)
			if pos_x==espx and pos_y==espy:
				if tipo==1:
					snake.insertar_inicio(1,1)
					comida.push(str(espx)+","+str(espy))
				else:
					snake.eliminar(0)
					comida.pop()
					pass
				activado=False
				pass
			if pos_x==0 or pos_y==0 or pos_x==49 or pos_y==24:
				Records.encolar(comida.get_puntaje()*(1-dificultad)+(15+comida.get_puntaje())*dificultad,Nombre)
				snake.graficar()
				comida.graficar()
				key=27
				pass
			if dificultad==1:
				if (pos_x==15 or pos_x==35) and (pos_y==5 or pos_y==6 or pos_y==7 or pos_y==8 or pos_y==9 or pos_y==10 or pos_y==15 or pos_y==16 or pos_y==17 or pos_y==18 or pos_y==19 or pos_y==20):
					Records.encolar(15+comida.get_puntaje(),Nombre)
					snake.graficar()
					comida.graficar()
					key=27
				pass
			for x in range(0,snake.get_indice()):
				if pos_y==snake.obtener_pos(x,2) and pos_x==snake.obtener_pos(x,1):
					Records.encolar(comida.get_puntaje()*(1-dificultad)+(15+comida.get_puntaje())*dificultad,Nombre)
					snake.graficar()
					comida.graficar()
					key=27
					pass
				pass
			try:
				for x in range(0,snake.get_indice()+1):
					window.addch(snake.obtener_pos(x,2),snake.obtener_pos(x,1),'█')
					pass
			except Exception as e:
				key=27
				pass
			pass
		window=curses.endwin()

class Usuarios():
	"""docstring for Usuari"""
	def __init__(self):
		screen = curses.initscr()
		height = 10
		width=50
		pos_y=0
		pos_x=0
		window = curses.newwin(height,width,pos_y,pos_x)
		window.keypad(True)
		curses.noecho()
		curses.curs_set(0)
		window.border(0)
		window.nodelay(True)
		window.addstr(0,20,"Select User")
		window.addstr(1,16,"Press ESC to select")
		global User
		global Nombre
		iteracion=0
		key=-1
		while key!=27:
			window.addstr(3,2,"                                              ")
			window.addstr(3,20,"<--"+User.obtener_iteracion(iteracion)+"-->")
			Nombre=User.obtener_iteracion(iteracion)
			key=window.getch()
			if key==KEY_RIGHT:
				iteracion=iteracion+1
			elif key==KEY_LEFT:
				iteracion=iteracion-1
				pass
			pass
		window=curses.endwin()

class Score():
	"""docstring for Score"""
	def __init__(self):
		global Records
		screen = curses.initscr()
		height = 15
		width=50
		pos_y=0
		pos_x=0
		window = curses.newwin(height,width,pos_y,pos_x)
		window.keypad(True)
		curses.curs_set(0)
		curses.noecho()
		window.border(0)
		window.nodelay(False)
		window.addstr(0,22,"Records")
		for x in range(0,Records.get_tam()):
			nombreusuario=Records.get_user(x)
			record=str(Records.get_score(x))
			window.addstr(x+3,20,nombreusuario+": "+record)
			pass
		window.getch()
		window=curses.endwin()

class Bulk():
	"""docstring for Bulk"""
	def __init__(self):
		screen = curses.initscr()
		height = 10
		width=50
		pos_y=0
		pos_x=0
		window = curses.newwin(height,width,pos_y,pos_x)
		window.keypad(True)
		curses.curs_set(0)
		curses.echo()
		window.border(0)
		window.nodelay(False)
		window.addstr(2,13,"Ingrese nombre de archivo")
		window.addstr(4,13,"")
		key=window.getkey()
		archivo=""
		while key!="\n":
			archivo=archivo+str(key)	
			key=window.getkey()
			pass
		try:
			f=open(archivo)
			valor=f.read()
			valores=valor.split("\n")
			primero=False
			for x in valores:
				if primero==False or x=="":
					primero=True
				else:
					User.insertar(x)
					pass
				pass	
			window.addstr(6,13,"Usuarios ingresados")
			f.close()
		except Exception as e:
			window.addstr(6,13,"error"+str(e))
		window.getch()
		window=curses.endwin()


class Principal():
	global Records
	global dificultad
	while True:
		screen = curses.initscr()
		height = 10
		width=50
		pos_y=0
		pos_x=0
		window = curses.newwin(height,width,pos_y,pos_x)
		window.keypad(True)
		curses.curs_set(0)
		curses.noecho()
		window.border(0)
		window.nodelay(False)
		window.addstr(0,21,"Main Menu")
		window.addstr(3,10,"1) Play")
		window.addstr(4,10,"2) Scoreboard")
		window.addstr(5,10,"3) User selection")
		window.addstr(6,10,"4) Reports")
		window.addstr(7,10,"5) Bulk Loarding")
		window.addstr(7,10,"6) Exit")
		key=window.getkey()
		if key=="1":
			dificultad=0
			window=curses.endwin()
			juego=Jugar()
		elif key=="2":
			window=curses.endwin()
			socore=Score()
		elif key=="3":
			window=curses.endwin()
			seleccion=Usuarios()
		elif key=="4":
			window=curses.endwin()
			Records.graficar()
			User.graficar()
			try:		
				os.system('imagenserpiente.jpg')
				os.system('imagenscore.jpg')
				os.system('imagenPila.jpg')
				os.system('imagenusuarios.jpg')
			except Exception as e:
				raise			
		elif key=="5":
			window=curses.endwin()
			carga=Bulk()
		elif key=="6":
			window=curses.endwin()
			break
			pass
		pass

Principal()