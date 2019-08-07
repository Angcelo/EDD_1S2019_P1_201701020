import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

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

key=KEY_RIGHT
pos_x=5
pos_y=5
window.addch(pos_y,pos_x,'*')
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
	window.addch(pos_y,pos_x,'*')
	pass
window.endwin()