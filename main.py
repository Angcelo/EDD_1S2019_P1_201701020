import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_ENTER
import serpiente
import Usuarios

Nombre=""
User=Usuarios.usuarios()	


class Principal()
	screen = curses.initscr()
	height = 10
	width=60
	pos_y=0
	pos_x=0
	window = curses.newwin(height,width,pos_y,pos_x)
	window.keypad(True)
	curses.curs_set(0)
	curses.noecho()
	window.border(0)
	window.nodelay(True)
	window.addstr(3,5,"1) Play")
	window.addstr(3,5,"2) Scoreboard")
	window.addstr(3,5,"3) User selection")
	window.addstr(3,5,"4) Reports")
	window.addstr(3,5,"5) Bulk Loarding")

class Jugar():
	def __init__(self):
		global Nombre
		global User
		if  Nombre=="":
			screen = curses.initscr()
			height = 10
			width=60
			pos_y=0
			pos_x=0
			window = curses.newwin(height,width,pos_y,pos_x)
			window.keypad(True)
			curses.curs_set(0)
			window.border(0)
			window.addstr(3,5,"Introduzca un nombre presione enter para continuar")
			window.addstr(4,5," ")
			key=window.getkey()
			while key!="\n":
				key=window.getkey()
				Nombre=Nombre+str(key)
				pass
			User.insertar_inicio(Nombre)
			window=curses.endwin()
			pass
		screen = curses.initscr()
		height = 50
		width=50
		pos_y=0
		pos_x=0
		window = curses.newwin(height,width,pos_y,pos_x)
		window.keypad(True)
		curses.curs_set(0)
		curses.noecho()
		window.border(0)
		window.nodelay(True)
		snake=serpiente.ListaDoble()
		snake.insertar_inicio(3,1)
		snake.insertar_inicio(2,1)
		snake.insertar_inicio(1,1)
		key=KEY_RIGHT
		pos_x=snake.obtener_pos(2,1)
		pos_y=snake.obtener_pos(2,1)
		for x in range(0,snake.get_indice()+1):
			window.addch(snake.obtener_pos(x,2),snake.obtener_pos(x,1),'#')
			pass
		while key!=27:
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
				key=keystroke
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
			snake.cambiar_posicion()
			snake.editar_ultimo(pos_x,pos_y)
			try:
				for x in range(0,snake.get_indice()+1):
					window.addch(snake.obtener_pos(x,2),snake.obtener_pos(x,1),'#')
					pass
			except Exception as e:
				window=curses.endwin()
				pass
			pass
		window=curses.endwin()

class Usuarios():
	"""docstring for Usuari"""
	def __init__(self):
		screen = curses.initscr()
		height = 40
		width=40
		pos_y=0
		pos_x=0
		window = curses.newwin(height,width,pos_y,pos_x)
		window.keypad(True)
		curses.noecho()
		curses.curs_set(0)
		window.border(0)
		window.nodelay(True)
		user=Usuarios.usuarios()

Jugar()