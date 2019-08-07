import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import serpiente

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

snake=serpiente.ListaDoble()
snake.insertar_inicio(3,1)
snake.insertar_inicio(2,1)
snake.insertar_inicio(1,1)
key=KEY_RIGHT
pos_x=snake.obtener_pos(2,1)
pos_y=snake.obtener_pos(2,1)
window.addch(snake.obtener_pos(0,2),snake.obtener_pos(0,1),'*')
window.addch(snake.obtener_pos(1,2),snake.obtener_pos(1,1),'*')
window.addch(snake.obtener_pos(2,2),snake.obtener_pos(2,1),'*')
window.timeout(10000)
while key!=27:
	window.timeout(100)
	keystroke=window.getch()
	if keystroke is not -1:
		key=keystroke
		pass
	window.addch(pos_y,pos_x,' ')
	if key==KEY_RIGHT:
		pos_x=pos_x+1
	elif key==KEY_LEFT:
		pos_x=pos_x-1
	elif key==KEY_UP:	
		pos_y=pos_y-1
	elif key==KEY_DOWN:
		pos_y=pos_y+1
		pass
	snake.editar_ultimo(pos_x,pos_y)
	snake.cambiar_posicion()
	window.addch(pos_y,pos_x,'*')
	pass
window=curses.endwin()