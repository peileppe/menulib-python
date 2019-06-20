#!/usr/bin/env python
import curses
import menulib as m

menu_1=(
	"Demo->",
	"Color",
	"Audio",
	"Window")

menu_2=(
	"Window->",
	"Minimize",
	"Maximize",
	"Arrange",
	"Get Info")

menu_main=(
	"New File",
	"Edit",
	menu_1,
	menu_2,
	"Help",
	"Exit")

def main(self):
	win=curses.initscr()
	max_option=len(menu_main)
	max_length = m.longest_in_the_list(menu_main) + 4
	returned_option=-1
	while returned_option != (max_option-1):
		y,x = 0, 0 
		returned_option=m.run_menu(menu_main)
		if returned_option==0:
			listF=["New File","created"]
			m.display_box(listF)		
		elif returned_option==1:
			listF=["File","Edited"]
			m.display_box(listF)
		elif returned_option==2:
			y, x =returned_option, max_length
			returned_option=m.run_menu(menu_1[1:],x,y, True)
			if returned_option==0:
				listF=["Color","activated"]
				m.display_box(listF)
			elif returned_option==1:
				listF=["Audio","activated"]
				m.display_box(listF)			
		elif returned_option==3:
			y, x =returned_option, max_length
			returned_option=m.run_menu(menu_2[1:],x,y, True)
		elif returned_option==4:
			listF=["Help","use arrow key or number"]
			m.display_box(listF)			
	curses.endwin()

if __name__ == '__main__':
    curses.wrapper(main)
